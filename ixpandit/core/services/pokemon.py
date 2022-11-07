import httpx


class PokemonService:
    API_POKEMON = "https://pokeapi.co/api/v2/pokemon/{pokemon}"

    @classmethod
    async def get_pokemon_by_name(cls, pokemon: str) -> httpx.Response:
        async with httpx.AsyncClient() as aioclient:
            response = await aioclient.get(url=cls.API_POKEMON.format(pokemon=pokemon))
            return response
