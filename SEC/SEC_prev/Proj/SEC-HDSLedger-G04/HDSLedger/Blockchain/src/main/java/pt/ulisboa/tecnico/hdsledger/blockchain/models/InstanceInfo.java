package pt.ulisboa.tecnico.hdsledger.blockchain.models;


import pt.ulisboa.tecnico.hdsledger.communication.CommitMessage;

public class InstanceInfo {

    private int currentRound = 1;
    private int preparedRound = -1;
    private String preparedValue;
    private CommitMessage commitMessage;
    private String inputValue;
    private int committedRound = -1;
    private String leaderId;

    public InstanceInfo(String inputValue) {
        this.inputValue = inputValue;
    }

    public InstanceInfo(String inputValue, String leaderId) {
        this.inputValue = inputValue;
        this.leaderId = leaderId;
    }

    public int getCurrentRound() {
        return currentRound;
    }

    public void setCurrentRound(int currentRound) {
        this.currentRound = currentRound;
    }

    public int getPreparedRound() {
        return preparedRound;
    }

    public void setPreparedRound(int preparedRound) {
        this.preparedRound = preparedRound;
    }

    public String getPreparedValue() {
        return preparedValue;
    }

    public void setPreparedValue(String preparedValue) {
        this.preparedValue = preparedValue;
    }

    public String getInputValue() {
        return inputValue;
    }

    public void setInputValue(String inputValue) {
        this.inputValue = inputValue;
    }

    public int getCommittedRound() {
        return committedRound;
    }

    public void setCommittedRound(int committedRound) {
        this.committedRound = committedRound;
    }

    public CommitMessage getCommitMessage() {
        return commitMessage;
    }

    public void setCommitMessage(CommitMessage commitMessage) {
        this.commitMessage = commitMessage;
    }

    public String getLeaderId() {
        return leaderId;
    }

    public void setLeaderId(String leaderId) {
        this.leaderId = leaderId;
    }
}
