class FoolException extends Exception {

}

public class ErrorSample {
    public void sayNick(String nick) throws FoolException {
        if ("바보".equals(nick)) {
            throw new FoolException();
        }
        System.out.println("당신의 별명은 "+nick+" 입니다.");

        System.out.println("당신의 별명은 "+nick+" 입니다.");
    }

    public static void main(String[] args) {
        ErrorSample sample = new ErrorSample();

        try {
            sample.sayNick("바보");
            sample.sayNick("야호");
        } catch (FoolException e) {
            System.out.println("FoolException이 발생했습니다.");
        }
    }
}
