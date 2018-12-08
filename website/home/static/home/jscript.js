$(document).ready(function(){
  $(window).on('scroll',function() {
    var scrolltop = $(this).scrollTop();

    if(scrolltop >= 215) {
      $('.fixedbar').fadeIn(250);
    }

    else if(scrolltop <= 210) {
      $('.fixedbar').fadeOut(250);
    }
  });

  $('.add_sym').click(function(){
	  $('.symptoms').append('<input type="text" class="sym">');
  });

  $('.age').change(function(){
	  var age = $(".age").children("option").filter(":selected").text();
	  $('input[name="gender"]').click(function(){
		  if(($(this).attr("value")=="female")&&((age=="Adolescent (13-16 years)")||(age=="Young Adult (17-29 years)")||(age=="Adult (30-39 years)")||(age=="Adult (40-49 years)")||(age=="Adult (50-64 years)"))){
			$('.preg').show();
		}
		  else{
			$('.preg').hide();
		}

		});
	  });


 $('section.navigation h4').click(function(event) {
	    event.preventDefault();
	    $(this).addClass('active');
	    $(this).siblings().removeClass('active');
	});

var formModal = $('.cd-user-modal'),
	formLogin = formModal.find('#cd-login'),
	formSignup = formModal.find('#cd-signup'),
	formForgotPassword = formModal.find('#cd-reset-password'),
	formModalTab = $('.cd-switcher'),
	tabLogin = formModalTab.children('li').eq(0).children('a'),
	tabSignup = formModalTab.children('li').eq(1).children('a'),
	forgotPasswordLink = formLogin.find('.cd-form-bottom-message a'),
	backToLoginLink = formForgotPassword.find('.cd-form-bottom-message a'),
	mainNav = $('.nav');
	nav2 = $('.fixedbar');
	nav3 = $('.fixednav');

	//open modal
	mainNav.on('click', function(event){
		$(event.target).is(mainNav) && mainNav.children('ul').toggleClass('is-visible');

	});

	//open sign-up form
	mainNav.on('click', '.cd-signup', signup_selected);
	//open login-form form
	mainNav.on('click', '.cd-signin', login_selected);

	nav2.on('click', function(event){
		$(event.target).is(nav2) && nav2.children('ul').toggleClass('is-visible');

	});

	//open sign-up form
	nav2.on('click', '.cd-signup', signup_selected);
	//open login-form form
	nav2.on('click', '.cd-signin', login_selected);


	nav3.on('click', function(event){
		$(event.target).is(nav3) && nav3.children('ul').toggleClass('is-visible');

	});

	//open sign-up form
	nav3.on('click', '.cd-signup', signup_selected);
	//open login-form form
	nav3.on('click', '.cd-signin', login_selected);


	//close modal
	formModal.on('click', function(event){
		if( $(event.target).is(formModal) || $(event.target).is('.cd-close-form') ) {
			formModal.removeClass('is-visible');
		}
	});
	//close modal when clicking the esc keyboard button
	$(document).keyup(function(event){
    	if(event.which=='27'){
    		formModal.removeClass('is-visible');

	    }
    });

	//switch from a tab to another
	formModalTab.on('click', function(event) {
		event.preventDefault();
		( $(event.target).is( tabLogin ) ) ? login_selected() : signup_selected();
	});

	//hide or show password
	$('.hide-password').on('click', function(){
		var togglePass= $(this),
			passwordField = togglePass.prev('input');

		( 'password' == passwordField.attr('type') ) ? passwordField.attr('type', 'text') : passwordField.attr('type', 'password');
		( 'Hide' == togglePass.text() ) ? togglePass.text('Show') : togglePass.text('Hide');
		//focus and move cursor to the end of input field
		passwordField.putCursorAtEnd();
	});

	//show forgot-password form
	forgotPasswordLink.on('click', function(event){
		event.preventDefault();
		forgot_password_selected();
	});

	//back to login from the forgot-password form
	backToLoginLink.on('click', function(event){
		event.preventDefault();
		login_selected();
	});

	function login_selected(){
		mainNav.children('ul').removeClass('is-visible');
		nav2.children('ul').removeClass('is-visible');
		nav3.children('ul').removeClass('is-visible');
		formModal.addClass('is-visible');
		formLogin.addClass('is-selected');
		formSignup.removeClass('is-selected');
		formForgotPassword.removeClass('is-selected');
		tabLogin.addClass('selected');
		tabSignup.removeClass('selected');
	}

	function signup_selected(){
		mainNav.children('ul').removeClass('is-visible');
		nav2.children('ul').removeClass('is-visible');
		nav3.children('ul').removeClass('is-visible');
		formModal.addClass('is-visible');
		formLogin.removeClass('is-selected');
		formSignup.addClass('is-selected');
		formForgotPassword.removeClass('is-selected');
		tabLogin.removeClass('selected');
		tabSignup.addClass('selected');
	}

	function forgot_password_selected(){
		formLogin.removeClass('is-selected');
		formSignup.removeClass('is-selected');
		formForgotPassword.addClass('is-selected');
	}

});
