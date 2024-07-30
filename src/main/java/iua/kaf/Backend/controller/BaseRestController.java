package iua.kaf.Backend.controller;

@RestController
@SecurityRequirement(name = "Bearer Authentication")
public class BaseRestController {

    @GetMapping(value = Constantes.URL_VERIFY, produces = MediaType.TEXT_PLAIN_VALUE)
    public ResponseEntity<String> verifyToken(@RequestParam(value = "token") String token) {
        return new ResponseEntity<String>(HttpStatus.OK);
    }
  
	
}
