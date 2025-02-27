# Transaction Notes

## 1. What are transactions?
A transaction is a sequence of database operations that are executed as a single logical unit of work. Transactions ensure data consistency, integrity, and reliability.

## 2. What are ACID Properties?
ACID stands for Atomicity, Consistency, Isolation, and Durability:
- **Atomicity**: Ensures that all operations within a transaction either complete fully or not at all.
- **Consistency**: Ensures that a transaction takes the database from one valid state to another.
- **Isolation**: Ensures that transactions do not interfere with each other.
- **Durability**: Ensures that committed transactions are permanently recorded, even in case of a system failure.

## 3. Suppose you do not have transactions. Is that system useful? Why?
Without transactions, a system might still function but would be prone to data corruption, inconsistencies, and partial failures. For example, in a banking system, transferring money without transactions could result in deducted amounts without crediting the recipient.

## 4. What properties does your file system have?
Most modern file systems support consistency mechanisms such as journaling (e.g., ext4, NTFS) to ensure data integrity. They may not strictly follow ACID but provide features like atomic writes and crash recovery.

## 5. Suppose you do not have "A" (Atomicity) in ACID. What happens? When is it okay?
Without atomicity, partial updates can occur, leading to data corruption. However, in systems where failures are rare and errors can be manually corrected, atomicity might not be critical. Example: A log system where partial writes are acceptable.

## 6. Suppose you do not have "C" (Consistency) in ACID. What happens? When is it okay?
Without consistency, the database might end up in an invalid state. However, eventual consistency (e.g., in distributed NoSQL databases) allows temporary inconsistencies that resolve over time, making it acceptable in high-availability systems.

## 7. Suppose you do not have "I" (Isolation) in ACID. What happens? When is it okay?
Without isolation, transactions might interfere with each other, leading to issues like dirty reads or lost updates. In real-time analytics, where immediate availability is more important than strict isolation, this might be acceptable.

## 8. Suppose you do not have "D" (Durability) in ACID. What happens? When is it okay?
Without durability, committed transactions might be lost after a system crash. However, for in-memory databases or caching layers where persistence is not required, this trade-off might be acceptable.
