import cv2

if __name__ == '__main__':
    i = 0
    cap = cv2.VideoCapture(0)
    while (1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)

        k = cv2.waitKey(1)
        if k == ord('s'):
            # 通过修改路径快速构造数据图像
            cv2.imwrite('RESIZED_DATASET/9/' + str(i) + '.jpg', frame)
            i += 1
            print("success!")
        elif k == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()