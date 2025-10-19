public class Gatto {
    private String nome;

    private static int numero_gatti = 0;

    public Gatto(String nome) {
        this.nome = nome;

        numero_gatti = numero_gatti + 1;
    }

    public static int getNumero_gatti() {
        return numero_gatti;
    }

    public String toString(){
        return nome + "\n";
    }
}
