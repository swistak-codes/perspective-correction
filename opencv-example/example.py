import cv2
import numpy as np

def main():
    # ścieka do obrazka
    input_image_path = 'sample_img.png'

    # punkty wyznaczające obszar, do którego chcemy przekształcić obraz
    x0, y0 = 146, 70
    x1, y1 = 583, 77
    x2, y2 = 41, 765
    x3, y3 = 687, 770

    # wczytanie obrazu do pamięci
    image = cv2.imread(input_image_path)
    if image is None:
        print("Nie można otworzyć obrazu.")
        return

    # pobranie wymiarów obrazu
    height, width = image.shape[:2]

    # punkty wyznaczające obszar
    points_src = np.array([
        [x0, y0],
        [x1, y1],
        [x2, y2],
        [x3, y3]
    ], dtype=np.float32)

    # punkty docelowe na rogach obrazu
    points_dst = np.array([
        [0, 0],
        [width, 0],
        [0, height],
        [width, height]
    ], dtype=np.float32)

    # obliczamy macierz transformacji
    M = cv2.getPerspectiveTransform(points_src, points_dst)

    # transformujemy obraz
    transformed_image = cv2.warpPerspective(image, M, (width, height))

    # złączamy oba obrazy w jeden
    combined_image = np.hstack((image, transformed_image))

    # wyświetlamy obrazy uzytkownikowi
    cv2.imshow('Oryginal i przetransformowany obraz', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()