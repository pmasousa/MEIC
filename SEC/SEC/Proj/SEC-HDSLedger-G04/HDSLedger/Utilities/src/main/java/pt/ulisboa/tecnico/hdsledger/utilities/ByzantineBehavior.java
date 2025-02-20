package pt.ulisboa.tecnico.hdsledger.utilities;

public enum ByzantineBehavior {
    NONE,
    IGNORE_REQUESTS,
    FAKE_LEADER, // starts proposing values despite not being the leader,
    BAD_LEADER_PROPOSE, // proposes a different value for each process
    BYZANTINE_UPON_PREPARE_QUORUM, // prepares with a wrong value for round r
    BYZANTINE_UPON_ROUND_CHANGE_QUORUM, // sets a wrong value 
}

// Implement behavior where the leader is byzantine and will not propose the value of the client, but will propose another one