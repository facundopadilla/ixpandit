from typing import Optional

from fastapi import APIRouter, status, Path, Request
from fastapi.responses import HTMLResponse

from ixpandit.core.settings.templates import templates
from ixpandit.core.services.pokemon import PokemonService

router = APIRouter(tags=["Index"])
pokemon_list = []  # simulate db


def _render_index(context: dict, status_code: Optional[int] = status.HTTP_200_OK) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        name="index.html",
        context=context,
        status_code=status_code
    )


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
async def index_view(request: Request):
    return _render_index(
        context={
            "request": request,
            "status_code": status.HTTP_200_OK,
            "pokemon_list": pokemon_list[:3]
        }
    )


@router.get(
    path="/{pokemon_name}",
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
async def index_view_search(request: Request, pokemon_name: str = Path(...)):
    response = await PokemonService.get_pokemon_by_name(pokemon=pokemon_name)
    if response.status_code == status.HTTP_404_NOT_FOUND:
        return _render_index(
            context={
                "request": request,
                "status_code": status.HTTP_404_NOT_FOUND,
                "error_detail": f"El pokemon '{pokemon_name}' no existe",
                "pokemon_list": pokemon_list[:3]
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
    pokemon_list.insert(0, response.json())
    return _render_index(
        context={
            "request": request,
            "status_code": status.HTTP_200_OK,
            "pokemon_list": pokemon_list[:3]
        }
    )
