var totalSum = 0;

    document.getElementById("expression").addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            calculate();
        }
    });

    function calculate() {
        var expression = document.getElementById("expression").value.trim();
        var num1, operation, num2;

        if (expression === "") {
            alert("Введите значение.");
            return;
        }

        if (expression.includes("+") || expression.includes("-") || expression.includes("*") || expression.includes("/")) {
            var parts = expression.split(/([+\-*/])/);
            num1 = parseFloat(parts[0]);
            operation = parts[1];
            num2 = parseFloat(parts[2]);

            if (isNaN(num1) || isNaN(num2)) {
                alert("Введите верное выражение. Пример '100*2'.");
                return;
            }
        } else {
            num1 = parseFloat(expression);
            operation = "";
            num2 = "";

            if (isNaN(num1)) {
                alert("Введите верное значение или выражение. Пример '100' или '100*2'.");
                return;
            }
        }

        var result;
        if (operation === "+") {
            result = num1 + num2;
        } else if (operation === "-") {
            result = num1 - num2;
        } else if (operation === "*") {
            result = num1 * num2;
        } else if (operation === "/") {
            if (num2 !== 0) {
                result = num1 / num2;
            } else {
                alert("Деление на ноль не допустимо.");
                return;
            }
        } else {
            // Если нет операции, просто использовать одно значение
            result = num1;
        }

        var historyList = document.getElementById("history");
        var historyItem = document.createElement("li");
        var calculation = document.createElement("span");
        calculation.textContent = String(num1.toFixed(2)) + " " + operation + " " + (num2 !== "" ? String(num2.toFixed(2)) : "") + " = " + String(result.toFixed(2));

        historyItem.appendChild(calculation);
        historyList.appendChild(historyItem);

        totalSum += result;
        document.getElementById("totalSum").textContent = String(totalSum.toFixed(2));

        document.getElementById("expression").value = "";
    }

    function resetHistory() {
        var historyList = document.getElementById("history");
        historyList.innerHTML = "";

        totalSum = 0;
        document.getElementById("totalSum").textContent = String(totalSum.toFixed(2));
    }

    function editCalculation(event) {
        var target = event.target;
        if (target.tagName === "SPAN") {
            var calculation = target.textContent;
            var parts = calculation.split(" ");
            var num1 = parseFloat(parts[0]);
            var operation = parts[1];
            var num2 = parseFloat(parts[2]);

            var expression = num1 + operation + num2;
            document.getElementById("expression").value = expression;

            target.parentNode.remove();

            totalSum -= eval(expression);
            document.getElementById("totalSum").textContent = String(totalSum.toFixed(2));
        }
    }