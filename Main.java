import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.io.*;

import java.util.Scanner;

public class Main {

    // Max amount of render possible.
    final static int max = 50;

    // Counter to keep track of current render.
    static int count = 0;

    // Path for the layers.
    // Path for the final renders.
    static String PATH = "D:\\imageGeneratorProject\\layers";
    static String outputPATH = "D:\\imageGeneratorProject\\renders";

    // Arraylist to store the "unique" image codes.
    static ArrayList<String> databaseImages = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();
    static Scanner input = new Scanner(System.in);


    public static void main(String[] args) throws IOException {

        start();
    }

    // Start the program.
    static void start() throws IOException {

        int duplications = 0;

        while (databaseImages.size() < max) {

            // Generate a random combination based on the images in the folder and child folders.
            // Then creates a string version of the combination.
            // These are separate arrays and do not rely on each other.
            int[] currentCombination = generateCombination();
            String stringCombination = arrayToString(currentCombination);

            // If the combination is not in the database, add it.
            if (!databaseImages.contains(stringCombination)) {

                count++;
                databaseImages.add(stringCombination);

                // Create the image.
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

    // This generates a random combination of images.
    // First, the parent folder's contents are added to the array, an array of folders if you will.
    // Next, an integer array is created to hold the "index" of the images in the child folders.
    // The index of an element in the array is the respective child folder.
    // Each integer element in the array represents the "index" of the image in the child folder.
    // The image is chosen at random within the child folder and is added to the integer array.
    // Finally, the integer array is returned.
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

    // This renders the images and saves them to the output folder.
    // First, the generated combination is used to get the images from the child folders.
    // Each image is added to an array of type File.
    // Next, a new canvas is created and the images are drawn on it.
    // Finally, the canvas is saved to the output folder.
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

    // This converts the integer array to a string.
    // This is used to check if the combination is unique.
    static String arrayToString(int[] array) {

        for (int n : array) {

            sb.append(n);
        }
        String stringCombination = String.valueOf(sb);
        sb.setLength(0);

        return stringCombination;
    }
}