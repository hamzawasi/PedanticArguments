FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
WORKDIR /PedanticArgsIdentity

COPY . ./

RUN sudo ./Web/PedanticArgsIdentity dotnet restore

RUN sudo ./Web/PedanticArgsIdentity dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /PedanticArgsIdentity
COPY --from=build-env /PedanticArgsIdentity/out .
ENTRYPOINT ["dotnet", "PedanticArgsIdentity.dll"]