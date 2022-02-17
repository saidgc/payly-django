// https://obfuscator.io/
var $inputService = document.getElementById('tel-input')
var $inputAmount = document.getElementById('amount-input')
var $discount = document.getElementById('discount_')
var $id = document.getElementById('service_id')

addEvent($inputAmount, "keyup", function (e) {
    if ($inputAmount.value > 300) {
        $("#right").show(300);
        $("#amount").html('$' + $inputAmount.value);
        $("#discount").html('-$' + ($inputAmount.value * ($discount.value / 100)).toFixed(2));
        $("#total").html('$' + ($inputAmount.value * (1 - $discount.value / 100)).toFixed(2));
    }
});

addEvent($inputService, "keyup", function (e) { check() });
addEvent($inputService, "paste", function (e) { check() });

function is_numeric(str) {
    return /^\d+$/.test(str);
}

function check() {
    $inputAmount.value = "";
    $("#right").hide(100);
    $("#no-valid").hide(100);
    $("#amount-label-uknow").hide(100);
    $("#amount-label-balance").hide(100);
    $("#amount-label-other").hide(100);
    if ($inputService.value.length === 10) {
        if (is_numeric($inputService.value)) {
            if (false) {
                $('#status-label').show(100);

                var requestOptions = {
                    method: 'GET',
                    redirect: 'follow'
                }

                fetch("/api/telmex/consultar?number=" + $inputService.value, requestOptions)
                    .then(response => response.text())
                    .then(result => {
                        var response = JSON.parse(result)
                        if (response['status'] == 'success') {
                            balance = response['balance']['importe']
                            $inputAmount.value = balance
                        }
                        if (response['balance']['error'] == "El Tel&eacute;fono no existe.") {
                            $('#status-label').hide(10);
                            $('#amount-label-uknow').show(10);
                            throw response['balance']['error']
                        }
                    })
                    .then(() => {
                        $('#status-label').hide(10);
                        $("#amount-label-uknow").hide(100);
                        $("#amount-label-balance").hide(100);
                        $("#amount-label-other").hide(100);
                        if (parseInt(balance) <= 0) {
                            $inputAmount.value = "";
                            $("#amount-label-balance").show(300);
                        } else if (parseInt(balance) > 300) {
                            $("#amount-label-balance").hide(10);
                            $("#right").show(300);
                            $("#amount").html('$' + balance);
                            $("#discount").html('-$' + (balance * ($discount.value / 100)).toFixed(2));
                            $("#total").html('$' + (balance * (1 - $discount.value / 100)).toFixed(2));
                            $("#amount-input").hide(100);
                            $("#amount-label").hide(100);
                        }
                    })
            } else {
                $('#status-label').hide(10);
                $('#amount-label-other').show(10);
                $("#amount-input").show(300);
                document.getElementById("amount-input").focus();
            }
        } else {
            $("#no-valid").show(100);
        }
    }
}

function addEvent(element, eventName, callback) {
    if (element.addEventListener) {
        element.addEventListener(eventName, callback, false);
    } else if (element.attachEvent) {
        element.attachEvent("on" + eventName, callback);
    } else {
        element["on" + eventName] = callback;
    }
}