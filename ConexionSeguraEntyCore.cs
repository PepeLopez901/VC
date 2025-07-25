// Modelo de ejemplo
public class Producto
{
    public int Id { get; set; }
    public string Nombre { get; set; }
}

// Contexto seguro
public class AppDbContext : DbContext
{
    public DbSet<Producto> Productos { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        // Usa el archivo de configuración o variables de entorno para la cadena de conexión
        var connectionString = Environment.GetEnvironmentVariable("DB_CONNECTION_STRING");
        optionsBuilder.UseSqlServer(connectionString);
    }
}

// Clase de servicio para productos
public class ProductoService
{
    // Uso seguro con using y async
    public async Task<List<Producto>> ObtenerProductosAsync()
    {
        using (var context = new AppDbContext())
        {
            return await context.Productos.ToListAsync();
        }
    }
}