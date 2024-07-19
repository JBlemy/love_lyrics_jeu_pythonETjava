package jeu_nombre_secret;

import java.util.Scanner;

public class Jeu_nombre_secret {
	
	public static void main(String[] args) {
		
		//Jeu nombre secret
		Scanner nb = new Scanner(System.in);
		
		int nbSecret, nbUtilisateur, rep;
		
		nbSecret = (int) (Math.random() * 999) + 1;
		
		System.out.print("\n\t\t\t\t\t\t*** Jeu nombre secret ***\n");
		do {
			do {
				
				System.out.print("\n\t\t\t\t\tEntrer un nombre entier entre 1 et 1000 :  ");
				nbUtilisateur = nb.nextInt();
				
				if (nbUtilisateur < nbSecret)
					System.out.print("\n\t\t\t\t\tVotre nombre est trop petit, reesayer.\n");
				else if (nbUtilisateur > nbSecret)
					System.out.print("\n\t\t\t\t\tVotre nombre est Trop grand, reesayer.\n");
				else
					System.out.print("\n\t\t\t\t\tFélicitation, vous avez gagné.\n");
				
			} while(nbSecret != nbUtilisateur);
			
			do{
				System.out.print("\n\n\n\n\n\n");
				System.out.print("\t\t\t\t\tVoullez vous faire une autre partie? (1 = oui, 0 = non).");
				System.out.print("\n\t\t\t\t\tFaites votre choix : ");
				rep = nb.nextInt();
				
				System.out.print("\n\n\n\n");
				
	            if(rep == 0 && rep != 1)
	            	System.out.print("\n\n\t\t\t\t\tMerci d'avoir utiliser notre jeu. Au revoir et a bientot...\n\n\n");
	          
	            else{
	                   if(rep != 0 && rep != 1){
	                	   System.out.print("\n\n\t\t\t\t\tVous devez choisir 1 pour continuer ou 0 pour quitter.\n\n");
	                }
	            }
	        } while(rep != 1 && rep != 0);
		} while(rep == 1);

	}

}
