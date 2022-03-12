// https://obfuscator.io/
/*var $inputService = document.getElementById('id_telmex_number')
var $inputAmount = document.getElementById('id_amount_to_pay')
var $discount = document.getElementById('discount_')
var $id = document.getElementById('service_id')*/

let client_whatsapp = document.getElementById('id_client_whatsapp')
let telmex_number = document.getElementById('id_telmex_number')
let amount_to_pay = document.getElementById('id_amount_to_pay')
let label_amount_to_pay = $('#label_id_amount_to_pay')
let discount = document.getElementById('id_service_discount')

telmex_number.addEventListener("keyup", event => {
    if (telmex_number.value.length === 10) {
        $(amount_to_pay).show()
        label_amount_to_pay.show()
    }
})

amount_to_pay.addEventListener("keyup", ev => {
    if (amount_to_pay.value > 100) {
        $("#right").show(300)
        $("#amount").html('$' + amount_to_pay.value)
        $("#discount").html('-$' + (amount_to_pay.value * (discount.value / 100)).toFixed(2))
        $("#total").html('$' + (amount_to_pay.value * (1 - discount.value / 100)).toFixed(2))
    } else {
        $("#right").hide(100)
    }
})

/*
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
    $("#id_amount_to_pay").hide(100);
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
                        $("#id_amount_to_pay").hide(100);
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
                $('#id_amount_to_pay').show(10);
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
}*/
