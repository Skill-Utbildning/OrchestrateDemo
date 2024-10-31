BEGIN
    LOAD DATA INFILE './data/account.csv'
    INTO TABLE account
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (AccountID, AccountNumber, CustomerID, Saldo);

    LOAD DATA INFILE './data/transactions.csv'
    INTO TABLE transactions
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (AccountNumber, Amount, TransactionDate);
END;