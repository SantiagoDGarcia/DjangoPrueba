
$(document).ready(function() {
    // Parametros del calendario
    $.datepicker.regional['es'] = {
        closeText: 'Cerrar',
        prevText: '< Ant',
        nextText: 'Sig >',
        currentText: 'Hoy',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
        dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
        weekHeader: 'Sm',
        dateFormat: 'dd/mm/yy',
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: ''
    };
    $.datepicker.setDefaults($.datepicker.regional['es']);
    // Funcion del calendario
    $( function() {
        $( "#id_fecha_compra" ).datepicker({dateFormat: 'dd/mm/yy'}); 
        $( "#id_fecha_venta" ).datepicker({dateFormat: 'dd/mm/yy'}); 
    });
    
    verificacionVenta();
    $("#id_vendido").click( function() {
        verificacionVenta();
    });
    function verificacionVenta() {
        if ($('#id_vendido').is(':checked')) {
            $('.form2 input').prop('disabled', false); // Doble verificaion, se desactivael inpu
            $('.form2').removeAttr('disabled'); // Se desactiva el div con el conteneido css
            $('.form2 :input').removeAttr('disabled');
        } else {
            $('.form2 :input').prop('disabled', true);
            $('.form2').attr('disabled', true);
        }   
    }

    $("#id_llego_cargador").click( function() {
        verificacionCargador1();
    });
    function verificacionCargador1() {
        if ($('#id_llego_cargador').is(':checked')) {
            $('#id_llego_cargador_rapido').prop('checked', false); // Doble verificaion, se desactivael inputt
        } 
    }

    $("#id_llego_cargador_rapido").click( function() {
        verificacionCargador();
    });
    function verificacionCargador() {
        if ($('#id_llego_cargador_rapido').is(':checked')) {
            $('#id_llego_cargador').prop('checked', false); // Doble verificaion, se desactivael inputt
        } 
    }

    $("#id_sefue_cargador").click( function() {
        verificacionCargadorSefue();
    });
    function verificacionCargadorSefue() {
        if ($('#id_sefue_cargador').is(':checked')) {
            $('#id_sefue_cargador_rapido').prop('checked', false); // Doble verificaion, se desactivael inputt
        } 
    }

    $("#id_sefue_cargador_rapido").click( function() {
        verificacionCargadorSefue2();
    });
    function verificacionCargadorSefue2() {
        if ($('#id_sefue_cargador_rapido').is(':checked')) {
            $('#id_sefue_cargador').prop('checked', false); // Doble verificaion, se desactivael inputt
        } 
    }

    $('.eliminar').click(function() { // Si hace click en cualquier "eliminar"
        $('.obscurecer').fadeIn(120); // Se activa la capa principal
        $('#fondo-eliminar' + $(this).attr('target')).fadeIn(150); // Se activa solo el id de esa capa
    });
    $('.obscurecer, #cancelar').click(function() { // Si hace click en cualquier parte de lo obscuro
        $('.obscurecer').fadeOut(150); // Se oculta esa capa
        $('.cuadro-eliminar').fadeOut(150); // Se oculta todas las clases del cuadro
    });

    $('.ver').click(function() { // Si hace click en cualquier "ver"
        $('.obscurecer').fadeIn(120); // Se activa la capa principal
        $('#fondo-ver' + $(this).attr('target')).fadeIn(150); // Se activa solo el id de esa capa
    });
    $('.obscurecer, #cancelar').click(function() { // Si hace click en cualquier parte de lo obscuro
        $('.obscurecer').fadeOut(150); // Se oculta esa capa
        $('.cuadro-ver').fadeOut(150); // Se oculta todas las clases del cuadro
    });
/*
    $('#tabla_datos').DataTable({
            "columnDefs": [
                { "orderable": false, "targets": [0, 2, 6, 7, 8, 9] },
                { "type": "date", "targets": 1 },
                {  "targets": [ 3 ], "visible": false },
                {  "targets": [6,7,8,9 ], "searchable": false },
            ],
            "language": {
                "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
            },
            "order": [[ 1, "desc" ], ],
            'info': false,
            "lengthMenu": [[-1,], ["Todos"]],
            //"dom": '<"top"i>rt<"bottom"flp><"clear">'
            //"dom": '<"top"i>rt<"bottom"flp><"clear">',
            'dom': 'Pfrtip',
            "scrollY":  "500px",
            "scrollCollapse": true,
            "paging": false,
    });
    
    var table = $('#tabla_datos').DataTable();
    table.on('draw', function () {
        let total = 0; let total2= 0; let total3 = 0;
        let datas = document.querySelectorAll(".classcompras");
        let datas2 = document.querySelectorAll(".classventas");
        let datas3 = document.querySelectorAll(".classganancias");
        for (let i = 0; i <datas.length; i++ ){
            total += parseFloat(datas[i].firstChild.data);
        }
        for (let i = 0; i <datas2.length; i++ ){
            total2 += parseFloat(datas2[i].firstChild.data);
        }
        for (let i = 0; i <datas3.length; i++ ){
            total3 += parseFloat(datas3[i].firstChild.data);
        }
        $("#compras").html( 'Compras: '+total );
        $("#ventas").html( 'Ventas: '+total2 );
        $("#ganancias").html( 'Ganancias: '+total3 );
    });
    */
});