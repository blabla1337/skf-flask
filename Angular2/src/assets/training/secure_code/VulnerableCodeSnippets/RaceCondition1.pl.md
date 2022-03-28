# Question
 
What is the problem here?
 
```
$transfer_amount = GetTransferAmount();
$balance = GetBalanceFromDatabase();

if ($transfer_amount < 0) {
	FatalError("Bad Transfer Amount");
}
$newbalance = $balance - $transfer_amount;
if (($balance - $transfer_amount) < 0) {
	FatalError("Insufficient Funds");
}
SendNewBalanceToDatabase($newbalance);
NotifyUser("Transfer of $transfer_amount succeeded.");
NotifyUser("New balance: $newbalance");
```
 
-----SPLIT-----
 
# Answer

It is a Race Condition Issue. This code could be used in an e-commerce application that supports transfers between accounts. It takes the total amount of the transfer, sends it to the new account, and deducts the amount from the original account. A race condition could occur between the calls to GetBalanceFromDatabase() and SendNewBalanceToDatabase(). https://cwe.mitre.org/data/definitions/362.html