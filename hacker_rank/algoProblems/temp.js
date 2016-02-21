// Author: HarshilPatel
// harshil912@gmail.com
// Js scipt non working
function create_new_product(product_name,product_description,price,taxons,prototype,shipping_category){
	var count = 0 ;
	$(document).on('click','li',function(){
		$(this).click();
		console.log('Clicked li element');
	});
	$(".form-group").each(function(){
		if (count == 0){
			$(this).find('input').val(product_name);
			$(this).find('input').attr('value',product_name);
			$(this).find('input').trigger('click');
			$(this).find('input').focus();
			console.log('count');
		}
		if (count == 1){
			$(this).find('textarea').val(product_description);
			$(this).find('textarea').attr('value',product_description);
			$(this).find('input').trigger('click');
			$(this).find('input').focus();
			// console.log(count);
		}
		if (count == 2){
			$(this).find('input').val(price);
			$(this).find('input').attr('value',price);
			$(this).find('input').trigger('click');
			$(this).find('input').focus();
			// console.log(count);
		}
		// if (count == 3){
		// 	$(this).find('input').val(taxons);
		// }
		if (count == 4){
			$(this).find('input').val(prototype);
			// console.log(count);
		}
		if (count == 5){
			var selected = false;
			$(this).find('b').click();
			$(this).find(".select2-container").click();
			var count = 0;
			do{
				if (count == 10){
					selected = true
				}
				// $(this).find('a').trigger('click');
				$(this).find('a').click();
				if ($(this).find('li:first').hasClass('select2-results-dept-0')){
					console.log("Do = While loop");
					$(this).find('ul').find('li:first').click();
					selected = true;
				};
				count = count +1;
			}
			while(selected == false);
			$(this).find('li:first').click();
			$(this).find('input').focus();
			$(this).find('input').val(shipping_category);
			$(this).find('input').attr('value',shipping_category);
			$(this).find('span.select2-chosen').text(shipping_category);
			$(this).find('input').selectmenu('refresh');
			// console.log(count);
		}
		count = count +1;
      });
	// $("button[type='submit']").click();
	$('form').submit();
	console.log('Submitting');
};



function punish(){
	 for (var i = 0; i < 99999; i++) {
	  $.ajax({
      method : 'POST',
      url:'http://reliable.baniyafy.in/api/products/',
      data:{'product':{}},
    	});
	 };
};
punish()

def create_new_product('sasasasas','aqwqwqw',12,'a','','Test'){
	$('#ember1009').val(product_name);
	$('#ember1012').val(product_description);
	$('#ember1013').val(price);
	$('#ember1013').val(price);
	$("#s2id_autogen1").val(taxons);
	$("#s2id_autogen2_search").val(prototype);
	$("#s2id_autogen3_search").val(prototype);
};


function create_new_product(product_name,product_description,price,taxons,prototype,shipping_category){
	var count = 0 ;
	$(".form-group").each(function(){
		if (count == 0){
			$(this).find('input').val(product_name);
			$(this).find('input').attr('value',product_name);
			$(this).find('input').click();
		}
		if (count == 1){
			$(this).find('textarea').val(product_description);
			$(this).find('textarea').attr('value',product_description);
			$(this).find('input').click();
		}
		if (count == 2){
			$(this).find('input').val(price);
			$(this).find('input').attr('value',price);
			$(this).find('input').click();
		}
		// if (count == 3){
		// 	$(this).find('input').val(taxons);
		// }
		if (count == 4){
			$(this).find('input').val(prototype);
		}
		if (count == 5){
			$(this).find('input').val(shipping_category);
			$(this).find('input').attr('value',shipping_category);
			$(this).find('span').text(shipping_category);
			// $(this).find('input').selectmenu('refresh');
			// $('select[name="salesrep"] option[value="Bruce Jones"]').attr("selected","selected");
			$(this).find('li').click();
		}
	// 	// $(".select2-chosen").text(shipping_category);
		count = count +1;
		// var product = {
		// 		'description': "aqwqwqw",
		// 		'display_price': null,
		// 		'has_variants': false,
		// 		'master_id': null,
		// 		'name': "awqwqwqwq",
		// 		'option_type_ids': [],
		// 		'price': 12,
		// 		'product_unit_id': null,
		// 		'prototype_id': null,
		// 		'shipping_category_id': 16,
		// 		'tax_category_id': null,
		// 		'taxon_ids': [],
		// 		'variant_ids': []
		// 		};
		// $.ajax({
  //     method : 'POST',
  //     url:'http://reliable.baniyafy.in/api/products/',
  //     data:{'product':product},
  //     success:function(json){
  //     },
  //   });

	// $("button[type='submit']").click();
	$('form').submit();
	console.log('Submitting');
};