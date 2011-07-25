
$(document).ready(function() {
	var sitecontacts_options = {
		dataType:  'json',
		success:   sitecontactsProcess, //What to call after a reply from Django
		beforeSubmit: sitecontactsBefore
	};
	$('#sitecontacts-form').ajaxForm(sitecontacts_options);
})

function sitecontactsBefore() {
	//$('#sitecontacts-form-submit').attr("disabled", "disabled");
	$('.errorlist').remove();
	$('tr.error').removeClass('error');
	return true;
}

function sitecontactsProcess(data) {
	if (data) {
		if (data.fail) {
			$.each(data.errs, function(fieldname, errmsg) {
				id = "#id_" + fieldname;
				$(id).after(errmsg);
			});
			$('#sitecontacts-form-submit').removeAttr("disabled");
		} else {
			//$('#sitecontacts-form').before('<div class="success">' + data.success + '</div>')
			//$('#sitecontacts-form').fadeOut()
		}
	} else {
		$('#sitecontacts-form').before('<div class="error">Ajax error: no data received.</div>')
		$('#sitecontacts-form').fadeOut()
	}
}
