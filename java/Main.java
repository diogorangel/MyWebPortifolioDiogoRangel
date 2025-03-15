import junit.framework.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.Scanner;
// import static org.junit.jupiter.api.Assertions.assertEquals;

// import org.junit.jupiter.api.Test;

public class Main {
  public static void main(String[] args) {
   Scanner entrada = new Scanner(System.in);
    System.out.println("Escolha uma opção: ");
    System.out.println("1 - Cadastrar Aluno" ");
    System.out.println("2 - Cadastrar Notas");
    System.out.println("Desejar Alunos e Notas");

    int numero = entrada.nextInt();
    swith(numero){
      case 1 ;
        System.out.println("Cadastrar Aluno");
        break;
      case 2 ;
        System.out.println("Cadastrar Notas");
      break;
      case 3 ;
        System.out.println("Listar Alunos");
      break;
      default;
      System.out.println("Opção Inválida");
    }
}