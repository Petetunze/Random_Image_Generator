import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

import java.util.Scanner;

public class Main {

    final static int max = 10;
    static int count = 0;

    static String PATH = "D:\\imageProject\\layers";
    static String outputPATH = "D:\\imageProject\\renders";

    static ArrayList<String> databaseImages = new ArrayList<>();
    static String[] currentImageMetadata = new String[8];
    static StringBuilder sb = new StringBuilder();
    static Scanner input = new Scanner(System.in);


    public static void main(String[] args) throws IOException {

        start();
    }

    // Start the program
    // Generates a combination that represents the image
    // and then renders the image and saves it to the output folder
    static void start() throws IOException {

        int duplications = 0;

        while (databaseImages.size() < max) {

            int[] currentCombination = generateCombination();
            String stringCombination = arrayToString(currentCombination);

            if (!databaseImages.contains(stringCombination)) {

                count++;
                databaseImages.add(stringCombination);

                render(currentCombination);

                System.out.println("Geode #" + count + " generated and saved!");
                System.out.println(count + "/" + max);
            }
            else{

                duplications++;
                System.out.println("Duplicate found. Rendering new image...");
            }
        }

        System.out.printf("\nDone!\nSuccessfully completed %d jobs\nDuplications: %d\n", Main.max, duplications);
    }

    // Generate a random combination of 8 numbers
    // Each number is unique to its respective layer
    static int[] generateCombination() {

        Random random = new Random();
        File[] parentDirectory = new File(PATH).listFiles();

        assert parentDirectory != null;
        int[] combination = new int[parentDirectory.length];

        for (int i = 0; i < combination.length; i++) {

            File[] files = new File(PATH + '\\' + parentDirectory[i].getName()).listFiles();

            assert files != null;
            int randomCharacteristic = random.nextInt(files.length);
            combination[i] = randomCharacteristic;
        }

        return combination;
    }

    // Takes an array of integers and renders the image based on the unique layers.
    static void render(int[] combination) throws IOException {

        File[] parentDirectory = new File(PATH).listFiles();
        BufferedImage[] images = new BufferedImage[combination.length];

        for (int i = 0; i < combination.length; i++) {

            assert parentDirectory != null;
            File[] imageFiles = new File(PATH + '\\' + parentDirectory[i].getName()).listFiles();

            assert imageFiles != null;
            images[i] = ImageIO.read(new File(PATH + '\\' + parentDirectory[i].getName(), imageFiles[combination[i]].getName()));
        }

        final int resolution = 2048;
        BufferedImage canvas = new BufferedImage(resolution, resolution, BufferedImage.TYPE_INT_ARGB);

        Graphics graphic = canvas.getGraphics();
        graphic.drawImage(images[0], 0, 0, null);
        for (int i = 1; i < images.length; i++) {

            graphic.drawImage(images[i], 32, 0, null);
        }

        ImageIO.write(canvas, "PNG", new File(outputPATH, "Geode #" + count + ".png"));
        graphic.dispose();
    }

    // Takes an array of integers and converts it to a string.
    static String arrayToString(int[] array) {

        for (int n : array) {

            sb.append(n);
        }
        String stringCombination = String.valueOf(sb);
        sb.setLength(0);

        return stringCombination;
    }
}