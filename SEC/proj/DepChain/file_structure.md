DepChain/
├── README.md
├── pom.xml
├── src/
│   ├── main/
│   │   └── java/
│   │       └── depchain/
│   │           ├── blockchain/
│   │           │   └── BlockchainMember.java
│   │           ├── client/
│   │           │   └── ClientLibrary.java
│   │           ├── consensus/
│   │           │   ├── ByzantineConsensus.java
│   │           │   ├── PerfectLinks.java
│   │           │   └── ConditionalCollect.java
│   │           ├── crypto/
│   │           │   └── CryptoUtils.java
│   │           ├── network/
│   │           │   ├── UDPSender.java
│   │           │   └── UDPReceiver.java
│   │           └── util/
│   │               └── Config.java
│   └── test/
│       └── java/
│           └── depchain/
│               └── tests/
│                   ├── BlockchainTest.java
│                   └── ConsensusTest.java
└── lib/   (if you include any additional libraries)
