

class SWPrinter implements Printer {
    public void print(String text) {
System.out.println("Printing in black and white: " + text);
}
}


class ColorPrinter implements Printer {
public void print(String text) {
System.out.println("Printing in color: " + text);
}
}


class PrinterProxy implements Printer {
private Printer printer;

public PrinterProxy(Printer printer) {
this.printer = printer;
}

public void print(String text) {
printer.print(text);
}

public void switchTo(Printer newPrinter) {
printer = newPrinter;
}
}


class Client {
public static void main(String[] args) {
Printer swPrinter = new SWPrinter();
Printer colorPrinter = new ColorPrinter();

PrinterProxy printer = new PrinterProxy(swPrinter);

printer.print("Hello world!"); // Prints "Printing in black and white: Hello world!"

printer.switchTo(colorPrinter);

printer.print("Hello world!"); // Prints "Printing in color: Hello world!"
}
}
