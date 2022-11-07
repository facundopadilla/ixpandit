import pytest
from fastapi.testclient import TestClient

from ixpandit.core.services.pokemon import PokemonService
from ixpandit.main import app


class TestIndexView:
    client = TestClient(app)

    @pytest.mark.asyncio
    async def test_pokemon_found_mocked(self, httpx_mock):
        httpx_mock.add_response(
            url=PokemonService.API_POKEMON.format(pokemon="peppa"),
            json={"name": "Peppa Pig", "sprites": {"front_default": "Sin imagen"}},
        )

        response = self.client.get(url="/peppa")

        assert (
            response.status_code == 200
            and "Peppa pig" in response.text
            and "Sin imagen" in response.text
        )

    @pytest.mark.asyncio
    async def test_pokemon_not_found_mocked(self, httpx_mock):
        httpx_mock.add_response(
            url=PokemonService.API_POKEMON.format(pokemon="mbappe"), status_code=404
        )
        response = self.client.get(url="/mbappe")
        assert (
            response.status_code == 404
            and "El pokemon &#39;mbappe&#39; no existe" in response.text
        )

    @pytest.mark.asyncio
    async def test_three_pokemons_in_list_and_not_found(self, httpx_mock):
        for pokemon in ["pikachu", "charmander", "snorlax", "mbappe"]:
            httpx_mock.add_response(
                status_code=200 if pokemon != "mbappe" else 404,
                url=PokemonService.API_POKEMON.format(pokemon=pokemon),
                json={"name": pokemon, "sprites": {"front_default": "Sin imagen"}},
            )
            self.client.get(url=f"/{pokemon}")

        response = self.client.get("/mbappe")
        assert (
            "Pikachu" in response.text
            and "Charmander" in response.text
            and "Snorlax" in response.text
            and "El pokemon &#39;mbappe&#39; no existe" in response.text
        )
