package binary;

public class BinaryMain {
	public static void main(String[] args) {
		int[] list = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		System.out.println("Position of the searched element: " + search(list, 8));
	}
	
	public static int search (int[] list, int elem) {
		int start = 0;
		int end = list.length - 1;	
		
		while (start <= end) {
			int mid = (start + end) / 2;
			if (list[mid] == elem) {
				return mid;
			} else if (list[mid] > elem) {
				end = mid - 1;
			} else {
				start = mid + 1;
			}
		}
		return -1;
	}
}
