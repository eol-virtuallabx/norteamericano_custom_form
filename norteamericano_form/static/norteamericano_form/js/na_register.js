$(document).ready(function() {
	function na_update_name(){
		var names = $('#register-na_names').val().trim();
		var last_name_p = $('#register-na_lastname_p').val().trim();
        var last_name_m = $('#register-na_lastname_m').val().trim();
		$('#register-name').val(names + ' ' + last_name_p + ' ' + last_name_m);
	}
	function check_rut_exists(rut){
		if (rut.charAt(0) == 'P'){
			rut = rut.toUpperCase();
            $('#register-na_rut').val(rut);
		}
		else{
			rut = clean_rut(rut).toUpperCase();
            $('#register-na_rut').val(format_rut(rut));
		}
		$.ajax({
			url: '/norteamericano_form/validate_rut/'+rut,
			type:'GET',
			success: function(resp) {
                if (resp.exists_rut){
                    $('#register-na_rut-validation-error-msg').text('RUT/Pasaporte ya existe.');
                    $('#register-na_rut').addClass('error na_error');
                    $('.text-na_rut label').addClass('error na_error');
                    $('#na_button')[0].disabled = true;
                }
                else{
                    $('#register-na_rut-validation-error-msg').text('');
                    $('#register-na_rut-validation-error-msg').removeClass('error_na_invalid');
                    $('#register-na_rut').removeClass('error na_error');
                    $('.text-na_rut label').removeClass('error na_error');
                    $('#na_button')[0].disabled = false;
                }
			},
			error: function() {
				alert('Un error inesperado ha ocurrido, actualice la página e intente nuevamente.')
				$('#register-na_rut-validation-error-msg').text('RUT/Pasaporte ya existe.');
                $('#register-na_rut').addClass('error na_error');
                $('.text-na_rut label').addClass('error na_error');
                $('#na_button')[0].disabled = true;
			}
		});
	}
	function na_on_change_na_rut(event){
        event.stopImmediatePropagation();
        $('#register-na_rut').val($('#register-na_rut').val().trim());
		var rut  = $('#register-na_rut').val().toUpperCase();
		if (rut !== null && typeof rut === 'string'){
            if (rut.charAt(0) == 'P'){
                if(rut.length < 6 || rut.length > 21){
                    $('#register-na_rut-validation-error-msg').text('');
                    $('#register-na_rut-validation-error-msg').addClass('error_na_invalid');
                    $('#register-na_rut').addClass('error na_error');
                    $('.text-na_rut label').addClass('error na_error');
                    $('#na_button')[0].disabled = true;
                }
                else{
                    check_rut_exists(rut)
                }
            }
            else if ((/^([\d]{1,2})(\.){0,1}([\d]{3})([.]{0,1})([\d]){3}([-]){0,1}([\dkK]){1}$/gm).test(rut) && validate_rut(format_rut(rut))){
                check_rut_exists(rut)
            }
            else{
                $('#register-na_rut-validation-error-msg').text('');
                $('#register-na_rut-validation-error-msg').addClass('error_na_invalid');
                $('#register-na_rut').addClass('error na_error');
                $('.text-na_rut label').addClass('error na_error');
                $('#na_button')[0].disabled = true;
            }
		}
		else{
            $('#register-na_rut-validation-error-msg').text('');
            $('#register-na_rut-validation-error-msg').addClass('error_na_invalid');
            $('#register-na_rut').addClass('error na_error');
            $('.text-na_rut label').addClass('error na_error');
            $('#na_button')[0].disabled = true;
        }
    }
	function na_check_update_birthdate(event){
		event.stopImmediatePropagation();
		$('#register-na_birth_date').val($('#register-na_birth_date').val().trim());
		var  new_date = $('#register-na_birth_date').val();
		if (new_date.trim() === ''){
			$('#register-na_birth_date').val('');
			$('#register-na_birth_date-validation-error-msg').text('Por favor ingresa Fecha Nacimiento.');
            $('#register-na_birth_date').addClass('error na_error');
            $('.text-na_birth_date label').addClass('error na_error');
			$('#register-na_birth_date-validation-error-msg').removeClass('error_na_invalid');
			return;
		}
		var r = /^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$/i;
	  	if (!r.test(new_date)){
			 $('#register-year_of_birth').val('');
			 $('#register-na_birth_date-validation-error-msg').text('');
			 $('#register-na_birth_date-validation-error-msg').addClass('error_na_invalid');
			 $('#register-na_birth_date').addClass('error na_error');
			 $('.text-na_birth_date label').addClass('error na_error');
	  	}
		else{
	  		var year = new_date.substring(6);
		 	var year_int = parseInt(year,10);
			var current_year = new Date().getFullYear();
			if(year_int >= 1900 && year_int <= current_year){
				$('#register-year_of_birth').val(year);
				$('#register-na_birth_date-validation-error-msg').text('');
				$('#register-na_birth_date-validation-error-msg').removeClass('error_na_invalid');
				$('#register-na_birth_date').removeClass('error na_error');
                $('.text-na_birth_date label').removeClass('error na_error');
			}
			else{
	 			$('#register-year_of_birth').val('');
				$('#register-na_birth_date-validation-error-msg').text('');
                $('#register-na_birth_date-validation-error-msg').addClass('error_na_invalid');
				$('#register-na_birth_date').addClass('error na_error');
				$('.text-na_birth_date label').addClass('error na_error');
			}
		}
	}

	var waitForEl = function(selector, callback) {
        if ($(selector).length) {
                callback();
        } else {
            setTimeout(function() {
                waitForEl(selector, callback);
            }, 100);
        }
    };
	waitForEl('#register-na_names',function(){
        $('#login-and-registration-container').on('change','#register-na_names',na_update_name);
    });
	waitForEl('#register-na_lastname_p',function(){
		$('#login-and-registration-container').on('change','#register-na_lastname_p',na_update_name);
	});
    waitForEl('#register-na_lastname_m',function(){
		$('#login-and-registration-container').on('change','#register-na_lastname_m',na_update_name);
	});
	waitForEl('#register-na_birth_date',function(){
		$('#login-and-registration-container').on('change','#register-na_birth_date',na_check_update_birthdate);
        });
	
	function clean_rut (rut) {
  		return typeof rut === 'string'? rut.replace(/^0+|[^0-9kK]+/g, '').toUpperCase(): '';
	}

	function validate_rut (rut) {
  		if (typeof rut !== 'string') {
            return false;
  		}
  		if (!/^0*(\d{1,3}(\.?\d{3})*)-?([\dkK])$/.test(rut)) {
            return false;
  		}

  		rut = clean_rut(rut);

  		var t = parseInt(rut.slice(0, -1), 10);
  		var m = 0;
  		var s = 1;

  		while (t > 0) {
            s = (s + (t % 10) * (9 - m++ % 6)) % 11;
            t = Math.floor(t / 10);
  		}

  		var v = s > 0 ? '' + (s - 1) : 'K';
  		return v === rut.slice(-1);
	}

	function format_rut (rut) {
  		rut = clean_rut(rut);
  		var result = rut.slice(-4, -1) + '-' + rut.substr(rut.length - 1);
  		for (var i = 4; i < rut.length; i += 3) {
    			result = rut.slice(-3 - i, -i) + '.' + result;
  		}

  		return result;
	}
    function format_rut_no_dots(rut) {
  		rut = clean_rut(rut);
  		var result = rut.slice(0, -1) + '-' + rut.substr(rut.length - 1);
        
  		return result;
	}
	var selector_rut  ='#register-form div.form-field.text-na_rut';
    var selector_button  ='#register-form button.register-button';
	waitForEl(selector_rut,function(){
		$('#login-and-registration-container').on('change','#register-na_rut',na_on_change_na_rut);
	});
    waitForEl(selector_button,function(){
		const aux_button = '<button type="button" id="na_button" class="action action-primary action-update js-register" disabled>Crear cuenta</button>';        
        $('#register')[0].insertAdjacentHTML('beforeend', aux_button);
        $('#na_button').on("click",function(e){
            e.stopPropagation();
            let na_rut = $('#register-na_rut').val()
            if (na_rut.charAt(0) != 'P'){
                $('#register-na_rut').val(format_rut_no_dots(na_rut));
            }
            $(selector_button)[0].click();
        });
	});
});