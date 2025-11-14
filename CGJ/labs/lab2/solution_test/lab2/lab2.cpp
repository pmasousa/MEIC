#include <iostream>
#include <stdexcept>
#include <string>
#include <cmath>

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

// ---------------------------------------------------------
// Global state for mouse-based rotation
// ---------------------------------------------------------
static float g_rotationAngle = 0.0f;      // angle in radians
static bool  g_isDragging = false;
static double g_lastX = 0.0;
static double g_lastY = 0.0;

// Sensitivity: radians per pixel of mouse movement
static const float ROTATION_SENSITIVITY = 0.01f;

// ---------------------------------------------------------
// Callbacks
// ---------------------------------------------------------

static void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    (void)window; // avoid unused warning
    glViewport(0, 0, width, height);
}

static void mouse_button_callback(GLFWwindow* window, int button, int action, int mods) {
    (void)mods; // unused

    if (button == GLFW_MOUSE_BUTTON_LEFT) {
        if (action == GLFW_PRESS) {
            g_isDragging = true;
            // Store current cursor position as reference
            glfwGetCursorPos(window, &g_lastX, &g_lastY);
        }
        else if (action == GLFW_RELEASE) {
            g_isDragging = false;
        }
    }
}

static void cursor_position_callback(GLFWwindow* window, double xpos, double ypos) {
    (void)window; // not used here, but kept for completeness

    if (g_isDragging) {
        double dx = xpos - g_lastX;
        // Optional: you could also use dy (ypos - g_lastY) for another axis

        g_rotationAngle += static_cast<float>(dx) * ROTATION_SENSITIVITY;

        g_lastX = xpos;
        g_lastY = ypos;
    }
}

// ---------------------------------------------------------
// Shader helpers
// ---------------------------------------------------------

static GLuint compileShader(GLenum type, const char* source) {
    GLuint shader = glCreateShader(type);
    glShaderSource(shader, 1, &source, nullptr);
    glCompileShader(shader);

    GLint success = 0;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
    if (!success) {
        GLint logLen = 0;
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &logLen);
        std::string log(logLen, '\0');
        glGetShaderInfoLog(shader, logLen, nullptr, &log[0]);
        std::cerr << "Shader compilation error: " << log << "\n";
        throw std::runtime_error("Failed to compile shader");
    }

    return shader;
}

static GLuint createProgram(const char* vertSrc, const char* fragSrc) {
    GLuint vs = compileShader(GL_VERTEX_SHADER, vertSrc);
    GLuint fs = compileShader(GL_FRAGMENT_SHADER, fragSrc);

    GLuint program = glCreateProgram();
    glAttachShader(program, vs);
    glAttachShader(program, fs);
    glLinkProgram(program);

    GLint success = 0;
    glGetProgramiv(program, GL_LINK_STATUS, &success);
    if (!success) {
        GLint logLen = 0;
        glGetProgramiv(program, GL_INFO_LOG_LENGTH, &logLen);
        std::string log(logLen, '\0');
        glGetProgramInfoLog(program, logLen, nullptr, &log[0]);
        std::cerr << "Program link error: " << log << "\n";
        throw std::runtime_error("Failed to link program");
    }

    glDeleteShader(vs);
    glDeleteShader(fs);

    return program;
}

// ---------------------------------------------------------
// main
// ---------------------------------------------------------

int main() {
    // 1. Inicializar GLFW
    if (!glfwInit()) {
        std::cerr << "Failed to initialize GLFW\n";
        return -1;
    }

    // OpenGL 3.3 Core Profile
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

    GLFWwindow* window = glfwCreateWindow(800, 600, "CGJ2025 - Mouse-rotated Triangle", nullptr, nullptr);
    if (!window) {
        std::cerr << "Failed to create GLFW window\n";
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
    glfwSetMouseButtonCallback(window, mouse_button_callback);
    glfwSetCursorPosCallback(window, cursor_position_callback);
    glfwSwapInterval(1); // vsync

    // 2. Inicializar GLEW (depois de criar o contexto)
    glewExperimental = GL_TRUE;
    GLenum glewStatus = glewInit();
    // GLEW pode gerar GL_INVALID_ENUM num core profile, limpamos o erro:
    glGetError();

    if (glewStatus != GLEW_OK) {
        std::cerr << "Failed to initialize GLEW: "
            << glewGetErrorString(glewStatus) << "\n";
        glfwDestroyWindow(window);
        glfwTerminate();
        return -1;
    }

    // 3. Info básica
    std::cout << "OpenGL version: " << glGetString(GL_VERSION) << "\n";
    std::cout << "GL Renderer: " << glGetString(GL_RENDERER) << "\n";

    glm::vec3 testVec(1.0f, 2.0f, 3.0f);
    std::cout << "GLM vec3 test: (" << testVec.x << ", "
        << testVec.y << ", "
        << testVec.z << ")\n";

    // 4. Shaders básicos (MVP + cor por vértice)
    const char* vertexShaderSrc = R"(#version 330 core
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;

uniform mat4 uMVP;

out vec3 vColor;

void main() {
    vColor = aColor;
    gl_Position = uMVP * vec4(aPos, 1.0);
}
)";

    const char* fragmentShaderSrc = R"(#version 330 core
in vec3 vColor;
out vec4 FragColor;

void main() {
    FragColor = vec4(vColor, 1.0);
}
)";

    GLuint program = 0;
    try {
        program = createProgram(vertexShaderSrc, fragmentShaderSrc);
    }
    catch (const std::exception& e) {
        std::cerr << "Error creating shader program: " << e.what() << "\n";
        glfwDestroyWindow(window);
        glfwTerminate();
        return -1;
    }

    // 5. Dados do triângulo: posições + cores
    float vertices[] = {
        // pos              // color
         0.0f,  0.366025f, 0.0f,  1.f, 0.f, 0.f,    // topo, vermelho
        -0.5f, -0.5f, 0.0f,  0.f, 1.f, 0.f,         // esquerda, verde
         0.5f, -0.5f, 0.0f,  0.f, 0.f, 1.f          // direita, azul
    };

    GLuint VAO = 0, VBO = 0;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    // layout(location = 0) -> posição (3 floats)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    // layout(location = 1) -> cor (3 floats)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float),
        (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);

    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);

    glEnable(GL_DEPTH_TEST);

    // 6. Loop principal
    while (!glfwWindowShouldClose(window)) {
        // Input básico: ESC para sair
        if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
            glfwSetWindowShouldClose(window, GLFW_TRUE);
        }

        // Get current window size
        int width, height;
        glfwGetFramebufferSize(window, &width, &height);

        // Calculate aspect ratio
        float aspect = 1.0f; // Default for safety
        if (height > 0) {
            aspect = (float)width / (float)height;
        }

        // Modelo: rotação controlada pelo rato (g_rotationAngle)
        glm::mat4 model = glm::rotate(glm::mat4(1.0f), g_rotationAngle, glm::vec3(0.0f, 0.0f, 1.0f));
        glm::mat4 view = glm::mat4(1.0f);

        // Keep the vertical height fixed
        float orthoHeight = 1.0f;
        // Adjust the width based on the aspect ratio
        float orthoWidth = orthoHeight * aspect;

        glm::mat4 proj = glm::ortho(-orthoWidth, orthoWidth,
            -orthoHeight, orthoHeight,
            -1.0f, 1.0f);
        glm::mat4 mvp = proj * view * model;

        // Limpar o ecrã
        glClearColor(0.1f, 0.15f, 0.25f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        // Usar o shader program
        glUseProgram(program);

        GLint mvpLoc = glGetUniformLocation(program, "uMVP");
        glUniformMatrix4fv(mvpLoc, 1, GL_FALSE, glm::value_ptr(mvp));

        // Desenhar triângulo
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 3);
        glBindVertexArray(0);

        // Swap buffers + eventos
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // 7. Cleanup
    glDeleteBuffers(1, &VBO);
    glDeleteVertexArrays(1, &VAO);
    glDeleteProgram(program);

    glfwDestroyWindow(window);
    glfwTerminate();

    return 0;
}