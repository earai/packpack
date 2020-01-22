FROM python:3.8-buster

ARG THIS_USER="packpacker"
ARG THIS_UID="1000"
ARG THIS_GID="100"
ENV HOME=/home/$THIS_USER

USER root

ADD ./bin/fix-permissions /usr/local/bin/fix-permissions
RUN chmod a+rx /usr/local/bin/fix-permissions

# include user code
ENV CODE_DIR=/opt/code/packpack

ADD . $CODE_DIR
WORKDIR $CODE_DIR

# lifted from https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile
RUN echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    touch /etc/sudoers && \
    sed -i.bak -e 's/^%admin/#%admin/' /etc/sudoers && \
    sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers && \
    useradd -m -s /bin/bash -N -u $THIS_UID $THIS_USER && \
    chown $THIS_USER:$THIS_GID /opt/code/packpack && \
    chmod g+w /etc/passwd
RUN fix-permissions $HOME
RUN fix-permissions "$(dirname $CODE_DIR)"

USER $THIS_UID

ENV PATH="/home/packpacker/.local/bin:$PATH"
RUN pip install --user --upgrade pip
RUN pip install --user pipenv
RUN pipenv install --system --dev --ignore-pipfile
RUN pip install --user -e .

#bind volume for easy development
VOLUME /opt/code/packpack
