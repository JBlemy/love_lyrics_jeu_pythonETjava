package jeu_capitale;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Jeu_capitale {
	
	public static void main(String[] args) {
		
		do {
		
		final int NOMBRE_DE_QUESTIONS = 7;
		int indice, score = 0;
		
		ArrayList<Integer> list_indice_deja_utiliser = new ArrayList<>(); //pour ne pas demander une meme pays plusieurs fois 
		
		String pays, capitale, rep_utilisateur;
		
		String[][] data = {
			{"Sénégal", "Dakar"},
			{"France", "Paris"},
			{"Russie", "Moscou"},
			{"Monaco", "Monaco"},
			{"Haiti", "Port-au-prince"},
			{"Pérou", "Lima"},
			{"Canada",  "Montreal"},
			
		}; 
		
		Scanner sc = new Scanner(System.in);
		
		for (int i = 0; i < NOMBRE_DE_QUESTIONS; i++) {
			do {
				Random valeur_aleatoire = new Random (); 
				indice = valeur_aleatoire.nextInt(data.length); //valeur aleatoire jusqu'a longueur chaine
			} while (list_indice_deja_utiliser.contains(indice)); //tant que l'indice a deja ete utiliser 
			
			list_indice_deja_utiliser.add(indice); //pour ajouter l'indice au tableau s'il n'etait pas dedans
			
			
			pays = data[indice][0]; //Pour recuperer le pays qui se trouve a cette indice 
			 capitale = data[indice][1]; //Pour recuperer la capitale qui se trouve a cette indice 
			
			System.out.printf("\nQuelle est la capitale de ce pays : %s ? \n" , pays);
			rep_utilisateur = sc.nextLine();
			
			if (capitale.equalsIgnoreCase(rep_utilisateur)) {
				System.out.println("Bravo, Bonne reponse !!!");
				score++;
			}
			
			else {
				System.out.printf("Mauvaise repopnse !!! Il fallait repondre %s. \n", capitale);
			}	
			
		}
		
		System.out.printf("\nC'est terminé, <<Score : %d/%d>> ", score, NOMBRE_DE_QUESTIONS);
		
	}while(demanderRepetition());
}
	static boolean demanderRepetition() {
	    Scanner nb1 = new Scanner(System.in);
	    int enr;
	    do {
	            System.out.print("\n\n\n\n\n\n");
	            System.out.print("\t\t\t\t\tPresser 1 pour rejouer, 0 pour quitter : ");
	            enr = nb1.nextInt();

	            System.out.print("\n\n\n\n");

	            if (enr == 0 && enr != 1) {
	                System.out.print("\n\n\t\t\t\t\tMerci d'avoir utilisé notre jeu. Au revoir et à bientôt...\n\n\n");
	                return false;
	            } 
	            
	            else {
	                if (enr != 0 && enr != 1) {
	                    System.out.print("\n\n\t\t\t\t\tVous devez choisir 1 pour rejouer ou 0 pour quitter.\n\n");
	                }
	            }
	    } while (enr != 1 && enr != 0);

	    return enr == 1;
	}

}
