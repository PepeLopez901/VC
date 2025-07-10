// ...existing code...
//Array simple
var ArrayTrimGuardar = [];
    
ArrayTrimGuardar.push({
    id: IdCtrl,
    Trim: i + 1,
    Bit_: Bit,
});

//switch simple numerico
switch (IntId) {
    case 1:
        break;
    case 2:
        break;
    case 3:
        break;
    case 4:
        break;
    case 5:
        break;
    case 6:
        break;
}

//Ajax
function ActualizarCierre(id) {
    var ServURL = Url;


    $.post(ServURL, {
        id: id
    },
    function (data) {
        if (data.exito == true) {
            
        }
        else {
           
        }
    }).fail(function () {
        
    });
}

//Obtener base64 de una imagen
function getBase64Image(img) {
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);
    var dataURL = canvas.toDataURL("image/png");
    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
}
//funcion 
function Fun() {}

// Array Simple
const Array = [];
$.each(ArrayResult, function (ind, elem) {
    Array.push(
      {
         Campo1: elem.Abonado,
         Campo2: elem.Credito,
         Campo3: elem.Fec_Factura,
         Campo4: elem.Folio,
         Campo5: elem.Id_Factura,
         Campo6: elem.Id_Fondo,
         Campo7: elem.Id_Pasivo,
         Campo8: elem.Id_Unidad_Ejecutora,
         Campo9: elem.Nombre,
      });
});


//Array de objetos
ArrayFac = [];
$.each(filasSeleccionadas, function (item, elem) {

   var controlId = "Div_" + elem.Id;
   var controlValue = $("#" + controlId).dxNumberBox("instance").option("value");

   ArrayFac.push(
      {
         Id_Factura: elem.Id,
         Txt_Importe: controlValue,
      });
});


//Formato de moneda
let Importe = 123456.78;
let formatMX = new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(Importe);

//Cambiar el DateTime de SQL a formato de fecha
function SQLFECHA(FecSQL_Date) {
   var FecSQL = new Date(parseInt(FecSQL_Date.substr(6)));
   //var FecSQL = Date(FecSQL2).toISOString();
   var dia = ("0" + FecSQL.getDate()).slice(-2);
   var mes = ("0" + (FecSQL.getMonth() + 1)).slice(-2);
   var año = FecSQL.getFullYear();
   var datestring = dia + "/" + mes + "/" + año
   return datestring;
}


//arreglo de fechas para un control de devextreme dxDateBox 
function RangoFechas(Fecha1, Fecha2, Days, ActiveDays) {
    var Fec1 = new Date(Fecha1);
    var Fec2 = new Date(Fecha2);
 
    var ActiveDay01 = new Date(ActiveDays[0].Fecha)
 
    let ArrayDias = Days.filter((n) => !ActiveDays.some((n2) => n.getTime() === (new Date(n2.Fecha)).getTime()));
 
    console.table(ArrayDias);
 
    $('#DivFec').dxDateBox("instance").option({ value: ActiveDay01, max: Fec2, min: Fec1, disabledDates: ArrayDias });
    //, 
 };

 function FunDiasEntreFechas(startDate, endDate) {
    const currentDate = new Date(startDate.getTime());
    const dates = [];
    while (currentDate <= endDate) {
       dates.push((new Date(currentDate)));
       console.log(currentDate);
       currentDate.setDate(currentDate.getDate() + 1);
    }
    return dates;
 }

 function FechasInscFin(Str_FecInicio, Str_Fec_Fin, ) {
    var FecInsc = new Date(Str_FecInicio);
    var FecInscDate = (((FecInsc.getMonth() + 1)).toString().padStart(2, '0') + "-" +
       (FecInsc.getDate()).toString().padStart(2, '0') + "-" +
       (FecInsc.getFullYear()).toString().padStart(2, '0'))
    var FecInscMilSec = new Date(FecInscDate).getTime();
 
    var FecFin = new Date(Str_Fec_Fin);
    var FecFinDate = (((FecFin.getMonth() + 1)).toString().padStart(2, '0') + "-" +
       (FecFin.getDate()).toString().padStart(2, '0') + "-" +
       (FecFin.getFullYear()).toString().padStart(2, '0'))
    var FecFinMilSec = new Date(FecFinDate).getTime();
 
    var DateNow = new Date();
    var FecNowDate = (((DateNow.getMonth() + 1)).toString().padStart(2, '0') + "-" +
       (DateNow.getDate()).toString().padStart(2, '0') + "-" +
       (DateNow.getFullYear()).toString().padStart(2, '0'))
    var FecNowMilSec = new Date(FecNowDate).getTime();
 
 };

 
function funPick(){
     const pick = (obj, keys) =>
    Object.keys(obj)
        .filter((k) => keys.includes(k))
        .reduce((res, k) => Object.assign(res, { [k]: obj[k] }), {});
}


var ArrayTipoContrato = ObjListCheck.map(function (item) {
    return pick(item, ["chkActivos", "Id_Tipo_Contrato"])
});

function getMondayOfCurrentWeek() {
    const today = new Date();
    const first = today.getDate() - today.getDay() + 1;

    const monday = new Date(today.setDate(first));
    return monday;
}

function Ajax(Id) {
    jQuery.ajax({
       dataType: 'json',
       data: { strId: Id },
       type: 'POST',
       url: UrlCboFondo,
       async: false,
       success: function (res) {
          if (res.exito == true) {
             if (res.result.length == 1) {
                
             }
          }
          else {
             
          }
       }
    }).fail(function () {
       errorPeticion(x, status, error);
    });
}

function AjaxAsync() {

    jQuery.ajax({
       dataType: 'json',
       data: { strId:  },
       type: 'POST',
       url: Url,
       async: false,
       success: function (res) {
          if (res.exito == true) {
            
             if (res.result.length == 1) {
             }
          }
          else {
             
          }
          panelCargaGenerico.hide();
       }
    }).fail(function () {
       panelCargaGenerico.hide();
       errorPeticion(x, status, error);
    });

}
 
//<% --check all-- %>

function selects() {
    var ele = document.getElementsByName('chk');
    for (var i = 0; i < ele.length; i++) {
        if (ele[i].type == 'checkbox') {
            if ($("#Chk").is(":checked") == true && ele[i].disabled == false) {
                ele[i].checked = true;
            }
            else {
                ele[i].checked = false;
            }
        }
    }
}

//<% --uncheck one-- %>

function deSelect() {
    var ele = document.getElementsByName('chkall');
    for (var i = 0; i < ele.length; i++) {
        if (ele[i].type == 'checkbox') {
            //ele[i].checked = false;
            if ($("#Chk").is(":checked") == true && ele[i].disabled == false) {
                ele[i].checked = true;
            }
            else {
                ele[i].checked = false;
            }
        }
    }
}

function SoloNumeros(evt) {
    var code = (evt.which) ? evt.which : evt.keyCode;
    if (code == 8) {
        return true;
    } else if (code >= 48 && code <= 57) {
        return true;
    } else {
        return false;
    }
}
//ocultar y mostrar conbtrol de devExpress
$("#btn_").dxButton("instance").option({ visible: true });
$("#btn_").dxButton("instance").option({ visible: false });
//Distinct
var ArrayDistinct  = Array.filter(
    (value, index, self) => self.findIndex(obj => obj.Id_ === value.Id_) === index
);
//string to boolean
(elem.Column).toLowerCase() === false

// Validar Row seleccionado
var ValSel = e.selectedRowKeys.length;
if (ValSel != null && ValSel != undefined && ValSel > 0) {
   var Selection = e.selectedRowKeys[0].Selecionable;

   if (Selection) {
      $("#btn_").dxButton("instance").option({ visible: true });
   } else {
    $("#btn_").dxButton("instance").option({ visible: false });
      e.component.clearSelection();
   }
}

const botones = {
    detalle: $("#btn_Detalle_").dxButton("instance"),
 };

botones.detalle.option({
    hint: "Autorizar",
    visible: true,
    text: "Autorizar",
    icon: ImgAutorizarProyecto,
    disabled: false
 });
