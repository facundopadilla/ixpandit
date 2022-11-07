from typing import Optional

from fastapi import APIRouter, Path, Request, status
from fastapi.responses import HTMLResponse

from ixpandit.core.services.pokemon import PokemonService
from ixpandit.core.settings.templates import templates
from ixpandit.core.utils.structures import SearchListInMemory

router = APIRouter(tags=["Index"])
pokemon_list = SearchListInMemory(max_size=3)  # simulate db


def _render_index(
    context: dict, status_code: Optional[int] = status.HTTP_200_OK
) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        name="index.html", context=context, status_code=status_code
    )


@router.get(path="/", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def index_view(request: Request):
    return _render_index(
        context={
            "request": request,
            "status_code": status.HTTP_200_OK,
            "pokemon_list": pokemon_list.elements(),
        }
    )


@router.get(
    path="/{pokemon_name}", status_code=status.HTTP_200_OK, response_class=HTMLResponse
)
async def index_view_search(request: Request, pokemon_name: str = Path(...)):
    response = await PokemonService.get_pokemon_by_name(pokemon=pokemon_name)
    if response.status_code == status.HTTP_404_NOT_FOUND:
        return _render_index(
            context={
                "request": request,
                "status_code": status.HTTP_404_NOT_FOUND,
                "error_detail": f"El pokemon '{pokemon_name}' no existe",
                "pokemon_list": pokemon_list.elements(),
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )

    pokemon_list.put(response.json())
    return _render_index(
        context={
            "request": request,
            "status_code": status.HTTP_200_OK,
            "pokemon_list": pokemon_list.elements(),
        }
    )
