// ...existing code...
//Llenar variable con un valor string y convertirlo a entero sino dejarlo null
int? Id = null; 
Id = string.IsNullOrEmpty(str) ? Id : Convert.ToInt32(str);

public class ListArray
{
    public int Id { get; set; }

    public int Id2 { get; set; }
    public string Importe { get; set; }
}
//For Each para recorrer un array de objetos
List<ListArray> Array = new List<ListArray>();
foreach (List ListArray in Array)
{
    suma = suma + Convert.ToDecimal(ListArray.Importe);
    ListFacturas.Add(new Generico_Type
    {
        campo1 = (Convert.ToInt32(ListArray.Id)).ToString(),
        campo2 = (Convert.ToDecimal(ListArray.Importe)).ToString(),
        campo3 = "",
        campo4 = "",
        campo5 = "",

    });
}
// return Json Incorrecto
return Json(new
{
    exito = false,
    message = ""
}, JsonRequestBehavior.AllowGet);
// return Json Correcto
return Json(new
{
    exito = true,
    message = ""
}, JsonRequestBehavior.AllowGet);

// ruta de archivo  
string NombreArchivo = "archivo.txt";
string ruta =
    Path.Combine(Server.MapPath("~/ruta/ruta"), "carpeta\\" + NombreArchivo);

 var mensajesError = new List<string>{ "Error 1.",
                                         "Error 2.",
                                         "Error 3."};

 if (mensajesError.Contains(SavePDF.ToString()))
 {
     return Save.ToString();
 }
// Crear un archivo PDF
 byte[] pdfB
using (var rptMemoryStream = new MemoryStream())
{
    // Exportar el reporte a PDF
    rpt.ExportToPdf(rptMemoryStream);
    rptMemoryStream.Position
    using (var pdfDocumentProcessor = new PdfDocumentProcessor())
    {
        pdfDocumentProcessor.CreateEmptyDocument();
        pdfDocumentProcessor.LoadDocument(rptMemoryStr);
        string directoryPath = Path.Combine(Server.MapPath("~/Archivos/"), "XML");
        Directory.CreateDirectory(directoryPath); // Ensure the directory e
        string filePath = Path.Combine(directoryPath, $"{NombreArchivo}.pdf");
        if (System.IO.File.Exists(filePath))
        {
            System.IO.File.Delete(filePath);

        pdfDocumentProcessor.SaveDocument(filePath);

    pdfBytes = rptMemoryStream.ToArray();

return File(pdfBytes, "application/pdf", $"{NombreArchivo}.pdf");



// store procedure EntityCore
using (var context = new Context())
{

    context.Database.EnsureCreated();
    FormattableString query = $"exec sp_name @param1, @param2";
    var result = context.Database.FromSql(query, param1, param2).asenumerable().where (x => x.Id == 1).ToList();
    return result;
}
using (var context = new Context())
{

    context.Database.EnsureCreated();
    SqlParameter param1 = new SqlParameter("@param1", 1);
    SqlParameter param2 = new SqlParameter("@param2", 2);  
    FormattableString query = $"exec sp_name @param1={param1}, @param2={param2}";
    var result = await context.Database.FromSqlRaw(query).asenumerable().where (x => x.Id == 1).ToList();
    return result;
}
using (var context = new Context())
{

    context.Database.EnsureCreated();
    SqlParameter param1 = new SqlParameter("@param1", 1);
    SqlParameter param2 = new SqlParameter("@param2", 2);
    SqlParameter paramOutPut = new SqlParameter("@param2", SqlDbType.Decimal){Direction = ParameterDirection.Output};  
    FormattableString query = $"exec sp_name @param1={param1}, @param2={param2}, @paramOutPut={paramOutPut} OUTPUT";
    var result = context.Database.ExecuteSqlAsync(query).asenumerable().where (x => x.Id == 1).ToList();
    return result;
}