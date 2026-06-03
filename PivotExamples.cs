using System;
using System.Collections.Generic;
using System.Data;
using System.Dynamic;
using System.IO;
using System.Linq;
using System.Text;

// Ejemplos de pivote con LINQ: columnas fijas, DataTable dinámico y exportar CSV.
class Sale { public string Month; public string Product; public decimal Amount; }

class MonthlySales
{
    public string Month { get; set; }
    public decimal Manzana { get; set; }
    public decimal Pera { get; set; }
    public decimal Naranja { get; set; }
    public override string ToString() => $"{Month} | Manzana={Manzana} | Pera={Pera} | Naranja={Naranja}";
}

class PivotExamples
{
    static void Main()
    {
        var sales = new List<Sale> {
            new Sale{ Month="2026-01", Product="Manzana", Amount=10 },
            new Sale{ Month="2026-01", Product="Pera", Amount=5 },
            new Sale{ Month="2026-01", Product="Naranja", Amount=8 },
            new Sale{ Month="2026-02", Product="Manzana", Amount=7 },
            new Sale{ Month="2026-02", Product="Naranja", Amount=12 },
        };

        Console.WriteLine("--- Pivote con clase MonthlySales (columnas fijas) ---");
        ExampleFixed(sales);

        Console.WriteLine();
        Console.WriteLine("--- Pivote a DataTable (columnas dinámicas) ---");
        ExampleDataTable(sales);

        Console.WriteLine();
        Console.WriteLine("--- Pivote dinámico exportado a CSV (pivot.csv) ---");
        ExampleCsv(sales);
        Console.WriteLine("CSV guardado en pivot.csv");
    }

    static void ExampleFixed(List<Sale> sales)
    {
        var pivot = sales
            .GroupBy(s => s.Month)
            .Select(g => new MonthlySales {
                Month = g.Key,
                Manzana = g.Where(x => x.Product == "Manzana").Sum(x => x.Amount),
                Pera = g.Where(x => x.Product == "Pera").Sum(x => x.Amount),
                Naranja = g.Where(x => x.Product == "Naranja").Sum(x => x.Amount)
            })
            .OrderBy(x => x.Month)
            .ToList();

        pivot.ForEach(Console.WriteLine);
    }

    static void ExampleDataTable(List<Sale> sales)
    {
        var products = sales.Select(s => s.Product).Distinct().ToList();
        var months = sales.Select(s => s.Month).Distinct().OrderBy(m => m);

        var table = new DataTable();
        table.Columns.Add("Month", typeof(string));
        foreach (var product in products) table.Columns.Add(product, typeof(decimal));

        foreach (var month in months)
        {
            var row = table.NewRow();
            row["Month"] = month;
            foreach (var product in products)
                row[product] = sales.Where(s => s.Month == month && s.Product == product).Sum(s => s.Amount);
            table.Rows.Add(row);
        }

        // Imprimir encabezados
        Console.WriteLine(string.Join(" | ", table.Columns.Cast<DataColumn>().Select(c => c.ColumnName)));
        foreach (DataRow r in table.Rows)
            Console.WriteLine(string.Join(" | ", r.ItemArray));
    }

    static void ExampleCsv(List<Sale> sales)
    {
        var products = sales.Select(s => s.Product).Distinct().ToList();

        var pivot = sales
            .GroupBy(s => s.Month)
            .Select(g => {
                dynamic obj = new ExpandoObject();
                var dict = (IDictionary<string, object>)obj;
                dict["Month"] = g.Key;
                foreach (var p in products)
                    dict[p] = g.Where(x => x.Product == p).Sum(x => x.Amount);
                return dict;
            })
            .OrderBy(d => d["Month"]) // orden por mes
            .ToList();

        var headers = new[] { "Month" }.Concat(products).ToArray();
        var sb = new StringBuilder();
        sb.AppendLine(string.Join(",", headers));
        foreach (var row in pivot)
            sb.AppendLine(string.Join(",", headers.Select(h => row[h]?.ToString() ?? "0")));

        File.WriteAllText("pivot.csv", sb.ToString(), Encoding.UTF8);
    }
}
