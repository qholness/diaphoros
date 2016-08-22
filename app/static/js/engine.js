var wage = 12;
var MaxSleepDebt = -0;



function cashIn() {
	/*Cash in the days work. Returning work to zero and adding money to bank account*/
	var work = document.getElementById('workCounter');
	var money = document.getElementById('moneyCounter');
	workedHours = parseFloat(work.innerHTML);
	moneyMade = parseFloat(money.innerHTML);

	money.innerHTML = moneyMade + wage * workedHours;
	work.innerHTML = 0;

}




function counter(id) {
	var counter = document.getElementById(id);
    function incrementcounter() {
    	currentValue = parseFloat(counter.innerHTML);
    	if (id=='sleep') {
    		if (currentValue < 12) {
    			var money = document.getElementById('moneyCounter');

    			counter.innerHTML = currentValue + 1;
    			money.innerHTML = parseFloat(money.innerHTML) - wage/4;
    		}
    	}
    	else {
       		counter.innerHTML = currentValue + .25;
       	}
    }
    incrementcounter();
}




function loseSleep() {
    function incrementsleep() {
	    var sleep = document.getElementById("sleep");
    	var sleepHours =  parseInt(sleep.innerHTML);
        sleep.innerHTML = --sleepHours;
        if (sleepHours > MaxSleepDebt) {
       		setTimeout(incrementsleep, 1000);
        }
   		if (sleepHours <= MaxSleepDebt) {
   			var again = confirm("Game Over.\nPlay Again?");
   			if (again) {
       			location.reload();
   			}
   			if (again == false) {
   				location("/");
   				return 0;
   			}
   		}
   		return 0;
    }

    incrementsleep();
}