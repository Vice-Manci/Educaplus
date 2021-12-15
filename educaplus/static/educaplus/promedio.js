import * as sys from 'sys';
var n1, n2, n3, n4, n5, n6, n7, result;
console.log("Herramienta para calcular promedio (usar valores no decimales.)");
n1 = Number.parseInt(input("Primera nota: "));
n2 = Number.parseInt(input("Segunda nota: "));
n3 = Number.parseInt(input("Tercera nota (dejar en cero si no existe): "));
n4 = Number.parseInt(input("Cuarta nota (dejar en cero si no existe): "));
n5 = Number.parseInt(input("Quinta nota (dejar en cero si no existe): "));
n6 = Number.parseInt(input("Sexta nota (dejar en cero si no existe): "));
n7 = Number.parseInt(input("Número de notas: "));
try {
    result = ((((((n1 + n2) + n3) + n4) + n5) + n6) / n7);
} catch(e) {
    if ((e instanceof ValueError)) {
        console.log("No se pueden usar n\u00fameros decimales, ni negativos");
    } else {
        if ((e instanceof ZeroDivisionError)) {
            console.log("Error: No se puede dividir entre cero.");
            sys.exit(1);
        } else {
            throw e;
        }
    }
}
console.log(`Tu promedio es ${result}`);

//# sourceMappingURL=promedio.js.map
