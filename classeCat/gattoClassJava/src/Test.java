public class Test {
    public static void main(String[] args) {
        Gatto g1 = new Gatto("Bob");
        Gatto g2 = new Gatto("Rob");

        System.out.println(g1);
        System.out.println(g2);

        System.out.println(Gatto.getNumero_gatti());
    }
}
