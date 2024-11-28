# CISC 7403 Course Project by Group B5

We develop a system that includes 3 microservices: voting, result and database.

## Dployment

After `git clone`-ing this repository, please run the following command to deploy the microservices.

```sh
cd CISC7403
docker-compose up -d
```

If you deploy the microservices locally, after the successful deployment, you can use `voting` on `http://127.0.0.1:6110/vote/`
and get the `result` from `http://127.0.0.1:6111/result/`. 

You can utilize `docker ps -a` to list all the containers and find the container ID of the voting container. 
Then, you can check the running log with `docker logs [Container ID]`.

## Code Structure

- `cloudproject`: the Django project provides voting service.
- `cloudproject02`: the Django project demonstrates voting results.
- `database`: used to build and initialize the Postgresql container.

## Acknowledgement

This project is implemented by LI Jingguang, Hoi Hou Hong, YE Fengying, and ZHANG Zihang.
Thanks for the lectures by Prof. Waynex ZHOU and the tutorials by TAs.
