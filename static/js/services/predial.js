var $inputService = document.getElementById('tel-input')
var $inputAmount = document.getElementById('amount-input')
var $discount = document.getElementById('discount_')

var $account = document.getElementById('account')
var $delegation = document.getElementById('delegation')
var $capture = document.getElementById('capture')
var $estateType = document.getElementById('estateType')


function consultarPredial() {
    $inputAmount.value = ""
    $("#right").hide(100)
    $("#consulta").hide(100)
    $('#status-label').show(100)
    $("#error-label").hide(100)
    var requestOptions = {
        method: 'GET'
    }
    if ($account.value != "" && $delegation.value != "") {
        fetch("/api/predialpuebla/consultar?account=" + $account.value + "&estate_type=" + $estateType.value + "&delegation=" + $delegation.value + "&capture_line=", requestOptions)
            .then(response => {
                console.log(response)
                if (response.ok) {
                    return response.text()
                }
                throw new Error('Error')
            })
            .then(result => { execute(result) })
            .catch(error => {
                console.log('error', error)
                $('#status-label').hide(10)
                $("#error-label").show(100)
            })

    } else if ($capture.value != "") {
        fetch("/api/predialpuebla/consultar?account=&estate_type=&delegation=&capture_line=" + $capture.value, requestOptions)
            .then(response => {
                console.log(response)
                if (response.ok) {
                    return response.text()
                }
                throw new Error('Error')
            })
            .then(result => { execute(result) })
            .catch(error => {
                console.log('error', error)
                $('#status-label').hide(10)
                $("#error-label").show(100)
            })
    }
}

function execute(result) {
    console.log(result)
    var response = JSON.parse(result)
    $("#error-label").hide(100)
    $('#status-label').hide(10)
    if (response.hasOwnProperty('total')) {
        $("#right").show(300)
        balance = parseFloat(response['total'].split(" ")[1].replace(',', ''))

        for (var key in response['charges']) {
            if (response['charges'].hasOwnProperty(key)) {
                var right = document.getElementById("right")
                var row = document.createElement("div")
                row.className = "row"

                var texto = key.charAt(0).toUpperCase() + key.slice(1).toLocaleLowerCase()

                var desc1 = document.createElement("p")
                var text1 = document.createTextNode(texto)
                desc1.appendChild(text1)

                var desc2 = document.createElement("strong")
                var text2 = document.createTextNode(response['charges'][key])
                desc2.appendChild(text2)

                row.appendChild(desc1)
                row.appendChild(desc2)

                right.insertBefore(row, right.children[1])
            }
        }

        $inputAmount.value = balance
        $("#discount").html('-$ ' + (balance * ($discount.value / 100)).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","))
        $("#total").html('$' + (balance * (1 - $discount.value / 100)).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","))
    } else if (response.hasOwnProperty('error')) {
        document.getElementById("error-label").innerHTML = response['error']
        $("#error-label").show(100)
        $('#status-label').hide(10)
        $("#consulta").show(300)
    }
}


// addEvent($inputAmount, "keyup", function (e) {
//     if (($account.value != "" && $delegation.value != "") || ($capture.value != "")) {
//         if ($inputAmount.value > 99) {
//             $("#right").show(300);
//             $("#amount").html('$' + $inputAmount.value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
//             $("#discount").html('-$' + ($inputAmount.value * ($discount.value / 100)).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
//             $("#total").html('$' + ($inputAmount.value * (1 - $discount.value / 100)).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
//         }
//     }
// });

// function addEvent(element, eventName, callback) {
//     if (element.addEventListener) {
//         element.addEventListener(eventName, callback, false);
//     } else if (element.attachEvent) {
//         element.attachEvent("on" + eventName, callback);
//     } else {
//         element["on" + eventName] = callback;
//     }
// }