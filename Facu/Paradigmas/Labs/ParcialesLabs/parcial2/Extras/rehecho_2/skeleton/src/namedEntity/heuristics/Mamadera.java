package namedEntity.heuristics;

public class Mamadera extends Heuristic {	
	
	protected boolean isEntity(String word){
		return (word.length() % 2 == 0);						
	}
	
}
