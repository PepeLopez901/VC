// ...existing code...
//Llenar variable con un valor string y convertirlo a entero sino dejarlo null
int? Id = null; 
Id = string.IsNullOrEmpty(str) ? Id : Convert.ToInt32(str);

public class ListArray
{
    public int Id { get; set; }
    public string Importe { get; set; }
}

public class Utilidades
{
    public static void GenerarLista()
    {
        List<Lists> Lista = new List<Lists>();

        for (int i = Int_01; i <= (Int_02 + 1); i++)
        {
            Lista.Add(new Lists
            {
                Num = (i),
                Text = (i).ToString()
            });
        }

        // Moved inside the method
        var result = new object(); // Placeholder, replace with actual result if needed
        Utils.GetJSONList(result, Lista.ToList());
    }

    public static void GetJSONList(object result, List<Lists> Lista)
    {
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

        // return Json(new
        // {
        //     exito = true,
        //     message = ""
        // }, JsonRequestBehavior.AllowGet);


    }

    public void ConvertirArchivo()
    {
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
        byte[] pdfB;
        using (var rptMemoryStream = new MemoryStream())
        {
            // Exportar el reporte a PDF
            rpt.ExportToPdf(rptMemoryStream);
            rptMemoryStream.Position;
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
                }
                else
                {
                    return Json(new
                    {
                        exito = false,
                        message = "El archivo no existe."
                    }, JsonRequestBehavior.AllowGet);
                }
            }
        }
    }

    public static void conexionEntityFramework()
    {
        // store procedure EntityCore
        using (var context = new Context())
        {

            context.Database.EnsureCreated();
            FormattableString query = $"exec sp_name @param1, @param2";
            var result = context.Database.FromSql(query, param1, param2).asenumerable().where(x => x.Id == 1).ToList();
            return result;
        }
        using (var context = new Context())
        {

            context.Database.EnsureCreated();
            SqlParameter param1 = new SqlParameter("@param1", 1);
            SqlParameter param2 = new SqlParameter("@param2", 2);
            FormattableString query = $"exec sp_name @param1={param1}, @param2={param2}";
            var result = await context.Database.FromSqlRaw(query).asenumerable().where(x => x.Id == 1).ToList();
            return result;
        }
        using (var context = new Context())
        {

            context.Database.EnsureCreated();
            SqlParameter param1 = new SqlParameter("@param1", 1);
            SqlParameter param2 = new SqlParameter("@param2", 2);
            SqlParameter paramOutPut = new SqlParameter("@param2", SqlDbType.Decimal) { Direction = ParameterDirection.Output };
            FormattableString query = $"exec sp_name @param1={param1}, @param2={param2}, @paramOutPut={paramOutPut} OUTPUT";
            var result = context.Database.ExecuteSqlAsync(query).asenumerable().where(x => x.Id == 1).ToList();
            return result;
        }
    }

    // Ejemplo de cadena de conexión (NO la pongas en el código en producción)
    // string connectionString = "Server=localhost;Database=MiBaseDatos;User Id=usuario;Password=contraseña;Encrypt=True;TrustServerCertificate=False;";

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        var connectionString = Environment.GetEnvironmentVariable("DB_CONNECTION_STRING");
        optionsBuilder.UseSqlServer(connectionString);
    }

    public class ProductoService
    {
        // Llama a un stored procedure y retorna los productos
        public async Task<List<Producto>> ObtenerProductosPorSPAsync()
        {
            using (var context = new AppDbContext())
            {
                // Si el SP no requiere parámetros:
                var productos = await context.Productos
                    .FromSqlRaw("EXEC NombreDelStoredProcedure")
                    .ToListAsync();

                // Si el SP requiere parámetros:
                // var productos = await context.Productos
                //     .FromSqlRaw("EXEC NombreDelStoredProcedure @param1, @param2", 
                //         new SqlParameter("@param1", valor1),
                //         new SqlParameter("@param2", valor2))
                //     .ToListAsync();

                return productos;
            }
        }
    }
    public class AppDbContext1 : DbContext
    {
        private readonly string _connectionString;
        public AppDbContext1(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(_connectionString);
        }
    }

    public class AppDbContext2 : DbContext
    {
        private readonly string _connectionString;
        public AppDbContext2(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("OtraConexion");
        }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(_connectionString);
        }
    }

    public void MultipleDbContexts(IConfiguration configuration)
    {
        using (var context1 = new AppDbContext1(configuration))
        {
            // Operaciones con la primera base de datos
        }
        using (var context2 = new AppDbContext2(configuration))
        {
            // Operaciones con la segunda base de datos
        }
    }
}








