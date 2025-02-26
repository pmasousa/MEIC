# DepChain

DepChain is a simplified permissioned blockchain system with high dependability guarantees. It is built using a layered architecture and implements a variant of the Byzantine Read/Write Epoch Consensus algorithm. This project is split into two stages. Stage 1 (this implementation) focuses on the consensus layer and basic blockchain member functionality.

## Features

- Authenticated perfect links over UDP
- Byzantine consensus for appending strings to the blockchain
- Client library for submitting append requests
- Basic cryptographic operations using the Java Crypto API

## Build and Run

- To compile the project, use Maven:

```
mvn clean install
```

- To run a blockchain member:

```
java -cp target/DepChain-1.0.jar depchain.blockchain.BlockchainMember
```

- To run the client:

```
java -cp target/DepChain-1.0.jar depchain.client.ClientLibrary
```

## Tests

Run the tests using:

```
mvn test
```

## Design

See the accompanying report for design decisions and threat analysis.
