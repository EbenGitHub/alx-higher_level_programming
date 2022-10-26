$(document).ready(function() {
	const url = "https://stefanbohacek.com/hellosalut/?";
	$("INPUT#btn_translate").click(function () {
		let valueInput = $("INPUT#language_code").val()
		let fullUrl = (url + "lang=" + valueInput)
		$.get(fullUrl, function(data) {
			$("DIV#hello").text(data.hello)
		})
	});

})
