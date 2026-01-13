## Learnings from this challenge

Bitcoin has multiple networks that all use the same software:

- mainnet: Real Bitcoin
- testnet: Public testing network
- regtest: Local private blockchain
- signet: Custom, permissioned test network

**Signet** = “Signed Testnet.”

It behaves like Bitcoin mainnet but only blocks signed by a specific key are accepted. A bitcoin.conf config file dictates the settings and allows the command "bitcoind -signet" to connect to a private Bitcoin universe.

**tprv** = extended private key for testnet/signet. Base58Check-encoded. Decoding this is just unpacking a data structure and reading fields that already exist.

**master chaine code** = a chain code is 32 bytes of cryptographic entropy that works together with a private key to generate child keys. An HD wallet is this pair: (master_private_key, master_chain_code). If you only used a private key to derive children, then if one child private key is leaked, attackers could reverse-engineer your master key. The chain code prevents that.

### Some notes about hierarchical deterministic (HD) wallets

An HD wallet is a structured tree of keys where every key is mathematically derived from a single root seed.

It is organized like a tree, every key has children, every branch has sub-branches.

Every key is fully determined by the master seed, which means Same seed → same wallet → same addresses → same funds. No randomness after setup. No need to store individual private keys. One backup restores everything.

Deriving a key and chaincode at a path means cryptographically generating new keys using the parent private key and the parent chain code that we decoded. The tprv only gives the root of the tree whereas the descriptor tells you which branch of the infinite tree to compute (which path down the tree to take). 

tprv decode → master_private_key, master_chain_code
derivation  → branch_private_key, branch_chain_code


