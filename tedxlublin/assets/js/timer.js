        // Set the date we're counting down to (example: December 31, 2024 23:59:59)
        var countDownDate = new Date("August 3, 2024 13:00:00").getTime();

        // Update the countdown every 1 second
        var x = setInterval(function() {
            var now = new Date().getTime();
            var distance = countDownDate - now;

            var months = Math.floor(distance / (1000 * 60 * 60 * 24 * 30.44));
            var days = Math.floor((distance % (1000 * 60 * 60 * 24 * 30.44)) / (1000 * 60 * 60 * 24));
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            document.getElementById("months").innerHTML = months.toString().padStart(2, '0');
            document.getElementById("days").innerHTML = days.toString().padStart(2, '0');
            document.getElementById("hours").innerHTML = hours.toString().padStart(2, '0');
            document.getElementById("minutes").innerHTML = minutes.toString().padStart(2, '0');
            document.getElementById("seconds").innerHTML = seconds.toString().padStart(2, '0');


        }, 1000);