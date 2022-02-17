var $inputService = document.getElementById('tel-input');
var $inputAmount = document.getElementById('amount-input');
var $discount = document.getElementById('discount_');
var $id = document.getElementById('service_id')

addEvent($inputAmount, "keyup", function (e) {
    if ($inputAmount.value > 99) {
        $("#right").show(300);
        $("#amount").html('$' + $inputAmount.value);
        $("#discount").html('-$' + ($inputAmount.value * ($discount.value / 100)).toFixed(2));
        $("#total").html('$' + ($inputAmount.value * (1 - $discount.value / 100)).toFixed(2));
        // window.scrollTo(0, document.body.scrollHeight);
    }

});

addEvent($inputService, "keyup", function (e) {
    $inputAmount.value = "";
    $("#right").hide(100);
    if ($inputService.value.length == 10) {
        if ($id.value != "6IpK0smbJQ00mAeDa81g") {
            $("#amount-label").hide(100);
        }
        $('#status-label').show(100);

        var formdata = new FormData()
        formdata.append("number", $inputService.value)

        var requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
        }

        fetch("/api/payly/getAmount", requestOptions)
            .then(response => response.text())
            .then(result => {
                balance = JSON.parse(result).amount;
                $inputAmount.value = balance;
            }
            ).then(() => {
                $('#status-label').hide(10);
                if (balance > 0) {
                    $("#right").show(300);
                    $("#amount").html('$' + balance);
                    $("#discount").html('-$' + (balance * ($discount.value / 100)).toFixed(2));
                    $("#total").html('$' + (balance * (1 - $discount.value / 100)).toFixed(2));
                    $("#amount-input").hide(100);
                    $("#amount-label").hide(100);
                    // window.scrollTo(0, document.body.scrollHeight);
                } else {
                    $inputAmount.value = "";
                    $("#amount-label").show(300);
                    if ($id.value != "6IpK0smbJQ00mAeDa81g") {
                        document.getElementById("amount-label").innerHTML = document.getElementById("amount-label").innerHTML.replace('Tu línea no tiene saldo pendiente o no fue encontrada, verifica de nuevo.', 'Introduce el monto de tu recibo')
                        $("#amount-input").show(300);
                        document.getElementById("amount-input").focus();
                    }
                }
            })
            .catch(error => {
                console.log(error)
                $('#status-label').hide(10);
                $inputAmount.value = "";
                $("#amount-label").show(300);
                if ($id.value != "6IpK0smbJQ00mAeDa81g") {
                    document.getElementById("amount-label").innerHTML = document.getElementById("amount-label").innerHTML.replace('Tu línea no tiene saldo pendiente o no fue encontrada, verifica de nuevo.', 'Introduce el monto de tu recibo')
                    $("#amount-input").show(300);
                    document.getElementById("amount-input").focus();
                }
                // document.getElementById("oxxobtn").style.display = 'inline';
            });
    }
});

addEvent($inputService, "paste", function (e) {
    $inputAmount.value = "";
    $("#right").hide(100);
    if ($inputService.value.length == 10) {
        $('#status-label').show(100);

        var formdata = new FormData()
        formdata.append("number", $inputService.value)

        var requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
        }

        fetch("/api/payly/getAmount", requestOptions)
            .then(response => response.text())
            .then(result => {
                balance = JSON.parse(result).amount;
                $inputAmount.value = balance;
            }
            ).then(() => {
                $('#status-label').hide(10);
                if (balance > 0) {
                    $("#right").show(300);
                    $("#amount").html('$' + balance);
                    $("#discount").html('-$' + (balance * ($discount.value / 100)).toFixed(2));
                    $("#total").html('$' + (balance * (1 - $discount.value / 100)).toFixed(2));
                    $("#amount-input").hide(100);
                    $("#amount-label").hide(100);
                    // window.scrollTo(0, document.body.scrollHeight);
                } else {
                    $inputAmount.value = "";
                    $("#amount-label").show(300);
                    if ($id.value != "6IpK0smbJQ00mAeDa81g") {
                        document.getElementById("amount-label").innerHTML = document.getElementById("amount-label").innerHTML.replace('Tu línea no tiene saldo pendiente o no fue encontrada, verifica de nuevo.', 'Introduce el monto de tu recibo')
                        $("#amount-input").show(300);
                        document.getElementById("amount-input").focus();
                    }
                }
            })
            .catch(error => {
                console.log(error)
                $('#status-label').hide(10);
                $inputAmount.value = "";
                $("#amount-label").show(300);
                if ($id.value != "6IpK0smbJQ00mAeDa81g") {
                    document.getElementById("amount-label").innerHTML = document.getElementById("amount-label").innerHTML.replace('Tu línea no tiene saldo pendiente o no fue encontrada, verifica de nuevo.', 'Introduce el monto de tu recibo')
                    $("#amount-input").show(300);
                    document.getElementById("amount-input").focus();
                }
                // document.getElementById("oxxobtn").style.display = 'inline';
            });
    }
});

function addEvent(element, eventName, callback) {
    if (element.addEventListener) {
        element.addEventListener(eventName, callback, false);
    } else if (element.attachEvent) {
        element.attachEvent("on" + eventName, callback);
    } else {
        element["on" + eventName] = callback;
    }
}