function sleepingPillBoost() {
	var money = document.getElementById('moneyCounter');
	var moneyValue = parseFloat(money.innerHTML);

	if (moneyValue >= 25) {
		// Increment sleep counter.
		// Subtract money for transaction
		var sleep = document.getElementById("sleep");
		sleep.innerHTML = parseInt(sleep.innerHTML) + 5;
		money = parseFloat(money.innerHTML) - 25;
	}
	else {
		alert("Not enough money");
	}


}