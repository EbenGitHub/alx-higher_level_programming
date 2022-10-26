$(document).ready(function() {
	const url = "https://stefanbohacek.com/hellosalut/?";
	$("INPUT#language_code").keyup(function(event) {
                if (event.keyCode === 13) {
                        $("INPUT#btn_translate").click();
                }
	});
	$("INPUT#btn_translate").click(function () {
		let valueInput = $("INPUT#language_code").val()
		let fullUrl = (url + "lang=" + valueInput)
		$.get(fullUrl, function(data) {
			$("DIV#hello").text(data.hello)
		})
	});

})
