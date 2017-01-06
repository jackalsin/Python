var display = null;

        var previousNumber = "";
        var currentOperator = "";
        var justPressedOperator = false;
        var calculationCompleted = false;
        function init()
        {
            display = $("#display")[0];

            var buttons = $("button");
            for(var i=0;i<buttons.length;i++)
            {
                buttons[i].onclick = buttonclicked;
            }
        }

        function calculation()
        {
            var firstNumber = parseFloat(previousNumber);
            var secondNumber = parseFloat(display.value);
            var result = 0;
            if(currentOperator == "+")
                result = firstNumber+secondNumber;
            else if(currentOperator == "-")
                result = firstNumber-secondNumber;
            else if(currentOperator == "*")
                result = firstNumber * secondNumber;
            else if(currentOperator == "/")
                result = firstNumber / secondNumber;
            
            display.value = result;

            calculationCompleted = true;

            return result;

        }

        function cleanOperatorBackground()
        {

            var operators = $(".operator");
            for(var i=0;i<operators.length;i++)
            {
                operators[i].style.backgroundColor = "";
            }
        }


        function buttonclicked(event)
        {
            var buttonContent = event.target.innerText;
            
            if(buttonContent == "." || (buttonContent >="0" && buttonContent <="9"))
            {

                if(justPressedOperator)
                {
                    display.value = "";
                    justPressedOperator = false;
                }
                if(calculationCompleted)
                {
                    display.value =buttonContent;                    
                    calculationCompleted = false;
                }
                else
                {
                    display.value = display.value+buttonContent;                
                }
                    
            }
            else if(buttonContent == "C")
            {
                previousNumber = "";
                currentOperator = "";
                justPressedOperator = false;
                display.value="";
                cleanOperatorBackground();
            }
            else if(buttonContent == "=")
            {
                if(previousNumber.length==0 || currentOperator.length==0 || display.value.length==0)
                {
                    return;
                }
                else
                {
                    calculation();

                    previousNumber = "";
                    currentOperator = "";

                    cleanOperatorBackground();
                }
            }
            else if(buttonContent >="*" && buttonContent <="/")
            {
                if(display.value.length==0)
                {
                    alert("Please enter a number first.");
                    return;
                }

                justPressedOperator = true;

                cleanOperatorBackground();

                event.target.style.backgroundColor ="gray";

                // An operator is pressed.
                if(previousNumber.length==0)
                {
                    previousNumber = display.value;
                    currentOperator = buttonContent;
                }
                else
                {
                    // Do the calculation.
                    previousNumber = calculation();
                    currentOperator = buttonContent;
                }
            }
        }
