package love;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Love {

	public static void main(String[] args) {
		
		do {
			ArrayList<Integer> list_indice_deja_utiliser = new ArrayList<>(); //pour ne pas demander une meme question plusieurs fois 
			
			System.out.print("\n\t\t\tHello mon coeur...Qu'est-ce que tu veux qu'on fasse Ou tu veux connaire à l'insant ??? \n\n");
			

			
			int reponse;
			do {
				Random valeur_aleatoire = new Random();
				 reponse = valeur_aleatoire.nextInt(51); //0 a 51-1
			} while(list_indice_deja_utiliser.contains(reponse));
			
			list_indice_deja_utiliser.add(reponse);
			
			System.out.println("\n\n\t\t\t Hmmm.... ");
			try {
				Thread.sleep(4000); //fais un pause de 4 seconde avant de continuer le reste du code
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			if (reponse == 0) 
				System.out.println("\t\t\t Fais moi un bisous.");
			
			if (reponse == 1)
				System.out.println("\t\t\t Fais moi un câlin.");
			
			if (reponse == 2) 
				System.out.println("\t\t\t Coucher sur moi.");
			
			if (reponse == 3) 
				System.out.println("\t\t\t Faisons l'amour.");
					
			if (reponse == 4) 
				System.out.println("\t\t\t Caresse moi.");
			
			if (reponse == 5) 
				System.out.println("\t\t\t Danse avec moi.");
			
			if (reponse == 6) 
				System.out.println("\t\t\t Faire quelque chose de votre choix.");
			
			if (reponse == 7) 
				System.out.println("\t\t\t Vérité ou action ? ");
			
			if (reponse == 8) 
				System.out.println("\t\t\t Dis moi quelque chose que personne ne sait sur toi.");
			
			if (reponse == 9) 
				System.out.println("\t\t\t Quel est votre plus grand secret? ");
			
			if (reponse == 10) 
				System.out.println("\t\t\t Que désiriez vous qu'on fasse à l'insant ? ");
			
			if (reponse == 11) 
				System.out.println("\t\t\t Dis moi je t'aime. ");
			
			if (reponse == 12) 
				System.out.println("\t\t\t Quel est le souvenir le plus précieux que tu aies de notre relation ? ");
			
			if (reponse == 13) 
				System.out.println("\t\t\t Y a-t-il quelque chose que tu voudrais changer dans notre relation ? ");
			
			if (reponse == 14) 
				System.out.println("\t\t\t Comment décrirais-tu notre relation à quelqu'un d'autre ? ");
			
			if (reponse == 15) 
				System.out.println("\t\t\t Quelle est la chose la plus romantique que tu aimerais faire pour moi ? ");
			
			if (reponse == 16) 
				System.out.println("\t\t\t Qu'est-ce qui te rend le plus fier(e) de nous en tant que couple ? ");
			
			if (reponse == 17) 
				System.out.println("\t\t\t Si tu pouvais me donner un seul conseil pour améliorer notre relation, quel serait-il ? ");
			
			if (reponse == 18) 
				System.out.println("\t\t\t Quelle est ta plus grande crainte concernant notre relation ?");
			
			if (reponse == 19) 
				System.out.println("\t\t\t En quoi notre relation t'a-t-elle transformé (e) ou changé (e) en tant que personne ?");
			
			if (reponse == 20) 
				System.out.println("\t\t\t Quel est ton premier souvenir de nous en tant que couple? ");
			
			if (reponse == 21) 
				System.out.println("\t\t\t Quelle est la chose la plus romantique que j'ai faite pour toi? ");
			
			if (reponse == 22) 
				System.out.println("\t\t\t Si tu pouvais revivre un moment romantique de notre relation, lequel choisirais-tu?");
			
			if (reponse == 23) 
				System.out.println("\t\t\t Quelle chanson, film ou livre te fait penser à notre relation? ");
			
			if (reponse == 24) 
				System.out.println("\t\t\t Quel est ton endroit préféré pour être avec moi? ");
			
			if (reponse == 25) 
				System.out.println("\t\t\tSi tu pouvais passer une journée parfaite avec moi, que ferions-nous? ");
			
			if (reponse == 26) 
				System.out.println("\t\t\t Quelle est ta vision de notre amour dans 10 ans? ");
			
			if (reponse == 27) 
				System.out.println("\t\t\t Comment décrirais-tu notre amour en un mot? ");
			
			if (reponse == 28) 
				System.out.println("\t\t\t Quelle est la chose la plus douce que j'ai faite pour toi? ");
			
			if (reponse == 29) 
				System.out.println("\t\t\t Quel est ton endroit préféré pour un rendez-vous romantique? ");
			
			if (reponse == 30) 
				System.out.println("\t\t\t Quelle est la qualité que tu aimes le plus en moi? ");
			
			if (reponse == 31) 
				System.out.println("\t\t\t Quel est ton plus beau souvenir de notre premier rendez-vous? ");
			
			if (reponse == 32) 
				System.out.println("\t\t\t Si tu pouvais changer une chose dans notre relation, que serait-ce? ");
			
			if (reponse == 33) 
				System.out.println("\t\t\t Quelle est la chose la plus importante que tu as apprise de notre relation? ");
			
			if (reponse == 34) 
				System.out.println("\t\t\t Quelle est ta plus grande peur en ce qui concerne notre relation? ");
			
			if (reponse == 35) 
				System.out.println("\t\t\t Si tu pouvais revivre un moment de notre relation, lequel choisirais-tu? ");
			
			if (reponse == 36) 
				System.out.println("\t\t\t Quel est ton surnom préféré pour moi? ");
			
			if (reponse == 37) 
				System.out.println("\t\t\t Si tu pouvais m'emmener n'importe où dans le monde, où irions-nous? ");
			
			if (reponse == 38) 
				System.out.println("\t\t\t Quel est ton plus grand rêve pour nous? ");
			
			if (reponse == 39) 
				System.out.println("\t\t\t Si tu devais me décrire en trois mots, quels seraient-ils?");
			
			if (reponse == 40) 
				System.out.println("\t\t\t Si tu pouvais écrire une chanson d'amour pour moi, comment s'appellerait-elle? ");
			
			if (reponse == 41) 
				System.out.println("\t\t\t Quelle est la chose la plus romantique que tu aies faite pour moi sans que je le sache? ");
			
			if (reponse == 42) 
				System.out.println("\t\t\t Si notre amour était une couleur, laquelle serait-elle et pourquoi? ");
			
			if (reponse == 43) 
				System.out.println("\t\t\t Quelle est la qualité que tu admires le plus chez moi? ");
			
			if (reponse == 44) 
				System.out.println("\t\t\t Quelle est la première chose qui t'a attiré(e) chez moi? ");
			
			if (reponse == 45) 
				System.out.println("\t\t\t Si nous devions écrire notre histoire d'amour, quel titre lui donnerions-nous?");
			
			if (reponse == 46) 
				System.out.println("\t\t\t Quelle est ta chanson d'amour préférée et pourquoi? ");
			
			if (reponse == 47) 
				System.out.println("\t\t\t Si tu pouvais inventer un jour spécial juste pour nous, que ferions-nous ce jour-là? ");
			
			if (reponse == 48) 
				System.out.println("\t\t\t Quel est ton souvenir de nous qui te fait sourire à chaque fois que tu y penses? ");
			
			if (reponse == 49) 
				System.out.println("\t\t\t Si tu devais créer un menu de dîner romantique pour nous, que servirais-tu? ");
			
			if (reponse == 50) 
				System.out.println("\t\t\t Si tu pouvais choisir un endroit dans le monde pour un dîner romantique, où irions-nous? ");
	} while(demanderRepetition());
}
	
	static boolean demanderRepetition() {
	    Scanner nb1 = new Scanner(System.in);
	    int enr;
	    do {
	            System.out.print("\n\n\n\n\n\n");
	            System.out.print("\t\t\t\t\tPresser 1 pour continuer, 0 pour quitter : ");
	            enr = nb1.nextInt();

	            System.out.print("\n\n\n\n");

	            if (enr == 0 && enr != 1) {
	                System.out.print("\n\n\t\t\t\t\tMerci d'avoir utilisé notre jeu d'amour. Au revoir et à bientôt...\n\n\n");
	                return false;
	            } 
	            
	            else {
	                if (enr != 0 && enr != 1) {
	                    System.out.print("\n\n\t\t\t\t\tVous devez choisir 1 pour continuer ou 0 pour quitter.\n\n");
	                }
	            }
	    } while (enr != 1 && enr != 0);

	    return enr == 1;
	}
}













