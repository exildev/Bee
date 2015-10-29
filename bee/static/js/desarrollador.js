var software;
$(document).on('ready',function(){
	$('.stop').on('click',function(){
		return false;
	});
	$('.solicitados').on('click',function(){
		cargarSolicitudes($(this));
	});
	software=$("#add_soft").dialog({
        autoOpen: false,
        draggable: false,
        modal:true,
        width:466,
        heigth:331,
        show: {
            effect: "slideDown",
            duration: 200
        },
        hide: {
            effect: "slideUp",
            duration: 200
        },
        buttons: {
            "OK": add_software_envio,
            "Cancelar":function(){
            	$(this).dialog("close");
            }
        },
        close:function(){
        	$(this).dialog('close')
        }
    });
	$('.registro_soft').on('click',function(){
		$('#buscar').load($(this).find('a').attr('href'),function(){
			/*$('.add_soft').on('click',function(){
				software.load('/form/agregar/software/',function(){
					add_software();
					software.dialog('open');
				});
			});*/
			cargarSofware();
		});
	});
	$('.medida').on('click',function(){
		$('#buscar').load($(this).find('a').attr('href'),function(){
			$('.seleccionar').on('click',function(){
				alert("click en la funcion");
				var nodo = $(this);
				var v =$(this).parent().find('input[type="hidden"]').val();
				$.ajax({
					url:'/desarrollar/solicitud/',
					type:'post',
					dataType:'json',
					data:{id:v},
					success:function(response){
						if(response[0].r){
							nodo.parent().find('div span').text("Desarrollando");
						};
					}
				});
			});
			$('#tabla_solicitud').dataTable();
			
		});
	})
	cargarSolicitudes($('.solicitados'));
	$(".paginate_button").on('click',function(event){
		$('#tabla').dataTable();
		$('.center.estado').on('click',function(){
			estadoRequerimiento($(this).parent().find('input[type="hidden"]'));
		});
	});
});


function cargarSolicitudes(r){
	$('#buscar').load(r.find('a').attr('href'),function(){
		$('#tabla').dataTable();
		$('.center.estado').on('click',function(){
			estadoRequerimiento($(this).parent().find('input[type="hidden"]'));
		});
	});
}

function estadoRequerimiento(r){
	$.ajax({
		url:"/ws/software/solicitados/",
		dataType:'json',
		data:{'r':r.val()},
		type:'post',
		success:function(response){
			cargarSolicitudes($('.solicitados'));
		}
	});
}

function add_software_envio(){
	$('#form').submit();
}

function close_soft(){
	var d= $('#dialog1').get(0);
	d.toggle();
}


function add_software(){
	var options1 = {
        beforeSubmit:function(){
        	alert("las function del submit");
        },
        success: function(response){
            if (/False/.test(response)){
            	if($('#add_soft #form ul li span').length == 0){
            		$('#add_soft #form ul').prepend('<li><span>* Todos los campos son requeridos</span></li>');
            	}
            	return;
            }
            software.dialog('close');
            cargarSofware();
        }
    };
    $('#form').ajaxForm(options1);
}

function cargarSofware(){
	$('#contenedor_cuerpo').load('/software/desarrollador/',function(){
        window.tabla_des = $('#tabla_des').dataTable();
    });
}
